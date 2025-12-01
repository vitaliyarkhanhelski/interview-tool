"""
Salesforce Interview Practice Tool - Main Application

This Streamlit application provides an AI-powered interactive interview practice platform
for Salesforce professionals. Users can simulate realistic job interviews with an AI HR
interviewer powered by Google Gemini 2.5 Flash.

Features:
    - Personalized interview setup (name, experience, skills, position, company)
    - Real-time streaming AI responses for natural conversation flow
    - Support for multiple Salesforce roles (Developer, Architect, Admin, QA, etc.)
    - Multiple target companies (Salesforce, Deloitte, Accenture, PwC, etc.)
    - Configurable interview length (default: 5 questions)
    - Detailed performance feedback with scoring (1-10 scale)
    - Beautiful Salesforce-themed UI with custom styling
    - Error handling for API availability issues
    - Session state management for seamless user experience

Workflow:
    1. User provides personal information and selects position/company
    2. AI conducts interview with role-appropriate questions
    3. User provides responses through chat interface
    4. After completion, user can request detailed feedback
    5. User can restart and practice unlimited times

Dependencies:
    - google-genai: For Google Gemini API integration
    - streamlit: For web application framework
    - streamlit-js-eval: For page reload functionality

Author: Vitaliy Arkhanhelski
"""

from google import genai

import streamlit as st
from streamlit_js_eval import streamlit_js_eval
from prompts import get_interview_system_prompt, build_feedback_prompt
from constants import *
from ui_components import info_box, info_box_small, feedback_box

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Load custom CSS
def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.title(MAIN_TITLE)

if "setup_complete" not in st.session_state:
    st.session_state.setup_complete = False
if "user_message_count" not in st.session_state:
    st.session_state.user_message_count = 0
if "feedback_shown" not in st.session_state:
    st.session_state.feedback_shown = False
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_complete" not in st.session_state:
    st.session_state.chat_complete = False

def complete_setup():
    st.session_state.setup_complete = True

def show_feedback():
    st.session_state.feedback_shown = True

if not st.session_state.setup_complete:
    st.subheader(SECTION_PERSONAL_INFO, divider=True)
    
    if "name" not in st.session_state:
        st.session_state["name"] = ""
    if "experience" not in st.session_state:
        st.session_state["experience"] = ""
    if "skills" not in st.session_state:
        st.session_state["skills"] = ""

    st.session_state["name"] = st.text_input(label=LABEL_NAME, placeholder=PLACEHOLDER_NAME, max_chars=MAX_CHARS_NAME, value=st.session_state["name"])
    st.session_state["experience"] = st.text_area(label=LABEL_EXPERIENCE, value=st.session_state["experience"], placeholder=PLACEHOLDER_EXPERIENCE, max_chars=MAX_CHARS_EXPERIENCE, height=None)
    st.session_state["skills"] = st.text_area(label=LABEL_SKILLS, value=st.session_state["skills"], placeholder=PLACEHOLDER_SKILLS, max_chars=MAX_CHARS_SKILLS, height=None)

    st.subheader(SECTION_COMPANY_POSITION, divider=True)
    
    if "position" not in st.session_state:
        st.session_state["position"] = DEFAULT_POSITION
    if "company" not in st.session_state:
        st.session_state["company"] = DEFAULT_COMPANY

    col1, col2 = st.columns(2)

    with col1:
        st.session_state["position"] = st.selectbox(LABEL_POSITION, JOB_POSITIONS)

    with col2:
        st.session_state["company"] = st.selectbox(LABEL_COMPANY, COMPANIES)

    if st.button(BUTTON_START_INTERVIEW, on_click=complete_setup):
        st.write(MESSAGE_SETUP_COMPLETE)


if st.session_state.setup_complete and not st.session_state.feedback_shown and not st.session_state.chat_complete:
    st.markdown(info_box(MESSAGE_INTRO), unsafe_allow_html=True)

    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

    if "gemini_model" not in st.session_state:
        st.session_state.gemini_model = GEMINI_MODEL

    if not st.session_state.messages:
        # System message
        st.session_state.messages = [{
            "role": "system",
            "content": get_interview_system_prompt()
        }]

    for message in st.session_state.messages:
        if message["role"] != "system":
            avatar = AVATAR_INTERVIEWER if message["role"] == "assistant" else AVATAR_USER
            with st.chat_message(message["role"], avatar=avatar):
                st.markdown(message["content"])


    if st.session_state.user_message_count < MAX_QUESTIONS:
        if prompt := st.chat_input(PLACEHOLDER_CHAT_INPUT, max_chars=CHAT_INPUT_MAX_CHARS):
            st.session_state.messages.append({"role": "user", "content": prompt})

            with st.chat_message("user", avatar=AVATAR_USER):
                st.markdown(prompt)

            if st.session_state.user_message_count < MAX_QUESTIONS - 1:
                with st.chat_message("assistant", avatar=AVATAR_INTERVIEWER):
                    try:
                        # Get system instruction
                        system_instruction = next((m["content"] for m in st.session_state.messages if m["role"] == "system"), "")
                        
                        # Build conversation history
                        conversation = "\n".join([
                            f"{'User' if m['role'] == 'user' else 'Assistant'}: {m['content']}"
                            for m in st.session_state.messages if m["role"] != "system"
                        ])
                        
                        # Create full prompt with system instruction
                        full_prompt = f"{system_instruction}\n\nConversation:\n{conversation}"
                        
                        # Call Gemini API with streaming
                        response = client.models.generate_content_stream(
                            model=st.session_state.gemini_model,
                            contents=full_prompt
                        )
                        
                        # Stream the response
                        full_response = ""
                        response_placeholder = st.empty()
                        for chunk in response:
                            if chunk.text:
                                full_response += chunk.text
                                response_placeholder.markdown(full_response)
                        
                        st.session_state.messages.append({"role": "assistant", "content": full_response})
                    except Exception as e:
                        error_message = str(e)
                        if "503" in error_message or "overloaded" in error_message.lower():
                            st.error(ERROR_AI_BUSY)
                        else:
                            st.error(f"{ERROR_GENERIC} {error_message}")
                        # Don't increment counter if there was an error
                        st.session_state.user_message_count -= 1
                        st.session_state.messages.pop()  # Remove the user message that failed
            
            st.session_state.user_message_count += 1
    
    if st.session_state.user_message_count >= MAX_QUESTIONS:
        st.session_state.chat_complete = True

if st.session_state.chat_complete and not st.session_state.feedback_shown:
    if st.button(BUTTON_GET_FEEDBACK, on_click=show_feedback):
        st.write(MESSAGE_FETCHING_FEEDBACK)

if st.session_state.feedback_shown:
    st.subheader(SECTION_FEEDBACK)
    
    try:
        feedback_client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
        
        feedback_prompt = build_feedback_prompt(st.session_state.messages)
        
        with st.spinner(MESSAGE_GENERATING_FEEDBACK):
            feedback_response = feedback_client.models.generate_content_stream(
                model=GEMINI_MODEL,
                contents=feedback_prompt
            )
        
            # Stream the feedback
            full_feedback = ""
            feedback_placeholder = st.empty()
            for chunk in feedback_response:
                if chunk.text:
                    full_feedback += chunk.text
                    # Wrap feedback in a styled box
                    feedback_placeholder.markdown(feedback_box(full_feedback), unsafe_allow_html=True)
    
    except Exception as e:
        error_message = str(e)
        if "503" in error_message or "overloaded" in error_message.lower():
            st.error(ERROR_AI_FEEDBACK_BUSY)
            if st.button(BUTTON_RETRY_FEEDBACK, type="secondary"):
                st.rerun()
        else:
            st.error(f"{ERROR_OCCURRED} {error_message}")
            st.markdown(info_box_small(INFO_RETRY), unsafe_allow_html=True)
    
    st.write("")  # Add spacing
    if st.button(BUTTON_RESTART_INTERVIEW, type="primary"):
        streamlit_js_eval(js_expressions="parent.window.location.reload()")