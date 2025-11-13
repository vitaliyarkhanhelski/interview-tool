from google import genai

import streamlit as st
from streamlit_js_eval import streamlit_js_eval

st.set_page_config(page_title="Streamlit Chat", page_icon="💬")
st.title("Chatbot")

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
    st.subheader("Personal Information", divider="rainbow")
    
    if "name" not in st.session_state:
        st.session_state["name"] = ""
    if "experience" not in st.session_state:
        st.session_state["experience"] = ""
    if "skills" not in st.session_state:
        st.session_state["skills"] = ""

    st.session_state["name"] = st.text_input(label="Name", placeholder="Enter your name", max_chars=40, value=st.session_state["name"])
    st.session_state["experience"] = st.text_area(label="Experience", value=st.session_state["experience"], placeholder="Describe your experience", max_chars=200, height=None)
    st.session_state["skills"] = st.text_area(label="Skills", value=st.session_state["skills"], placeholder="List your skills", max_chars=200, height=None)

    st.subheader("Company and Position", divider="rainbow")
    
    if "level" not in st.session_state:
        st.session_state["level"] = "Junior"
    if "position" not in st.session_state:
        st.session_state["position"] = "Data Scientist"
    if "company" not in st.session_state:
        st.session_state["company"] = "Amazon"

    col1, col2 = st.columns(2)

    with col1:
        st.session_state["level"] = st.radio("Choose Level", key="visibility", options=["Junior", "Mid-Level", "Senior"])


    with col2:
        st.session_state["position"] = st.selectbox("Choose a Position", ("Data Scientist", "Data Engineer", "ML Engineer", "BI Analyst", "Financial Analyst"))

    st.session_state["company"] = st.selectbox("Choose a Company", ("Amazon", "Meta", "Udemy", "365 Company", "Nestle", "LinkedIn", "Spotify"))

    if st.button("Start Interview", on_click=complete_setup):
        st.write("Setup complete. Starting interview...")


if st.session_state.setup_complete and not st.session_state.feedback_shown and not st.session_state.chat_complete:
    st.info(
        """
        Start by introducing yourself
        """
    )

    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

    if "gemini_model" not in st.session_state:
        st.session_state.gemini_model = "gemini-2.5-flash"

    if not st.session_state.messages:
        # System message
        st.session_state.messages = [{
            "role": "system",
            "content": f"You are an HR executive that interviews an interviewee called {st.session_state['name']} with experience {st.session_state['experience']} and skills {st.session_state['skills']}. You should interview them for the position {st.session_state['level']} {st.session_state['position']} at the company {st.session_state['company']}."
        }]

    for message in st.session_state.messages:
        if message["role"] != "system":
            avatar = "👔" if message["role"] == "assistant" else None
            with st.chat_message(message["role"], avatar=avatar):
                st.markdown(message["content"])


    if st.session_state.user_message_count < 5:
        if prompt := st.chat_input("Your answer:", max_chars=1000):
            st.session_state.messages.append({"role": "user", "content": prompt})

            with st.chat_message("user"):
                st.markdown(prompt)

            if st.session_state.user_message_count < 4:
                with st.chat_message("assistant", avatar="👔"):
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
                        
                        # Call Gemini API
                        response = client.models.generate_content(
                            model=st.session_state.gemini_model,
                            contents=full_prompt
                        )
                        
                        full_response = response.text
                        st.markdown(full_response)
                        
                        st.session_state.messages.append({"role": "assistant", "content": full_response})
                    except Exception as e:
                        error_message = str(e)
                        if "503" in error_message or "overloaded" in error_message.lower():
                            st.error("🔄 **The AI is temporarily busy.** Please wait a moment and try sending your message again.")
                        else:
                            st.error(f"❌ **Error:** {error_message}")
                        # Don't increment counter if there was an error
                        st.session_state.user_message_count -= 1
                        st.session_state.messages.pop()  # Remove the user message that failed
            
            st.session_state.user_message_count += 1
    
    if st.session_state.user_message_count >= 5:
        st.session_state.chat_complete = True

if st.session_state.chat_complete and not st.session_state.feedback_shown:
    if st.button("Get Feedback", on_click=show_feedback):
        st.write("Fetching feedback...")

if st.session_state.feedback_shown:
    st.subheader("Feedback")
    
    conversation_history = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages])
    
    try:
        feedback_client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
        
        system_instruction = """You are a helpful tool that provides feedback on an interviewee performance.
        Before the Feedback give a score of 1 to 10.
        Follow this format:
        Overal Score: //Your score
        Feedback: //Here you put your feedback
        Give only the feedback do not ask any additional questins.
        """
        
        feedback_prompt = f"{system_instruction}\n\nThis is the interview you need to evaluate. Keep in mind that you are only a tool and you should not engage to conversation. And you should provide feedback on the interviewee performance. Here is the conversation:\n\n{conversation_history}"
        
        with st.spinner("Generating your feedback..."):
            feedback_response = feedback_client.models.generate_content(
                model="gemini-2.5-flash",
                contents=feedback_prompt
            )
        
        st.write(feedback_response.text)
    
    except Exception as e:
        error_message = str(e)
        if "503" in error_message or "overloaded" in error_message.lower():
            st.error("🔄 **The AI service is currently busy.** Please wait a moment and click the button below to try again.")
            if st.button("🔄 Retry Feedback", type="secondary"):
                st.rerun()
        else:
            st.error(f"❌ **An error occurred:** {error_message}")
            st.info("Please try again or restart the interview.")

    if st.button("Restart Interview", type="primary"):
        streamlit_js_eval(js_expressions="parent.window.location.reload()")