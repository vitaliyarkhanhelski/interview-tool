"""
Constants and configuration for the Salesforce Interview Practice application.
Modify values here to customize the app.
"""

# ============================================================================
# INTERVIEW CONFIGURATION
# ============================================================================

MAX_QUESTIONS = 5  # Maximum number of interview questions


# ============================================================================
# JOB POSITIONS
# ============================================================================

JOB_POSITIONS = (
    "Junior Salesforce Developer",
    "Middle Salesforce Developer", 
    "Senior Salesforce Developer",
    "Salesforce Lead Developer",
    "Salesforce Architect",
    "Salesforce Business Analyst",
    "Salesforce Admin",
    "Salesforce QA Engineer",
    "Salesforce Consultant"
)

DEFAULT_POSITION = "Junior Salesforce Developer"


# ============================================================================
# COMPANIES
# ============================================================================

COMPANIES = (
    "Salesforce",
    "Deloitte Digital",
    "Accenture",
    "PwC",
    "Capgemini",
    "IBM",
    "Slalom",
    "CloudKettle",
    "Simplus"
)

DEFAULT_COMPANY = "Salesforce"


# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

PAGE_TITLE = "Salesforce Interview Practice"
PAGE_ICON = "☁️"
MAIN_TITLE = "☁️ Salesforce Interview Practice"


# ============================================================================
# SECTION HEADERS
# ============================================================================

SECTION_PERSONAL_INFO = "Personal Information"
SECTION_COMPANY_POSITION = "Company and Position"
SECTION_FEEDBACK = "Your Feedback"


# ============================================================================
# FIELD LABELS
# ============================================================================

LABEL_NAME = "Name"
LABEL_EXPERIENCE = "Experience"
LABEL_SKILLS = "Skills"
LABEL_POSITION = "Choose a Position"
LABEL_COMPANY = "Choose a Company"


# ============================================================================
# PLACEHOLDERS
# ============================================================================

PLACEHOLDER_NAME = "Enter your name"
PLACEHOLDER_EXPERIENCE = "Describe your experience"
PLACEHOLDER_SKILLS = "List your skills"
PLACEHOLDER_CHAT_INPUT = "Your answer:"


# ============================================================================
# BUTTON TEXT
# ============================================================================

BUTTON_START_INTERVIEW = "Start Interview"
BUTTON_GET_FEEDBACK = "Get Feedback"
BUTTON_RESTART_INTERVIEW = "Restart Interview"
BUTTON_RETRY_FEEDBACK = "🔄 Retry Feedback"


# ============================================================================
# MESSAGES
# ============================================================================

MESSAGE_INTRO = "Please first briefly introduce yourself"
MESSAGE_SETUP_COMPLETE = "Setup complete. Starting interview..."
MESSAGE_FETCHING_FEEDBACK = "Fetching feedback..."
MESSAGE_GENERATING_FEEDBACK = "Generating your feedback..."

# Info messages
INFO_RETRY = "Please try again or restart the interview."

# Error messages
ERROR_AI_BUSY = "🔄 **The AI is temporarily busy.** Please wait a moment and try sending your message again."
ERROR_AI_FEEDBACK_BUSY = "🔄 **The AI service is currently busy.** Please wait a moment and click the button below to try again."
ERROR_OCCURRED = "❌ **An error occurred:**"
ERROR_GENERIC = "❌ **Error:**"


# ============================================================================
# CHAT SETTINGS
# ============================================================================

CHAT_INPUT_MAX_CHARS = 1000
AVATAR_INTERVIEWER = "☁️"  # Salesforce cloud for interviewer
AVATAR_USER = "🧑‍💼"  # Professional person for candidate


# ============================================================================
# FIELD CONSTRAINTS
# ============================================================================

MAX_CHARS_NAME = 40
MAX_CHARS_EXPERIENCE = 200
MAX_CHARS_SKILLS = 200


# ============================================================================
# GEMINI MODEL
# ============================================================================

GEMINI_MODEL = "gemini-2.5-flash"

