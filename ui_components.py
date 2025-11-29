"""
UI Components for the Salesforce Interview Practice application.
Reusable styled HTML components.
"""

def info_box(message, icon="ℹ️"):
    """
    Creates a styled info box with Salesforce theme.
    
    Args:
        message: The text message to display
        icon: Optional emoji icon (default: ℹ️)
    
    Returns:
        HTML string for the info box
    """
    return f"""
        <div style="background-color: white; padding: 15px; border-left: 4px solid #00A1E0; border-radius: 4px; margin-bottom: 20px;">
            <p style="color: #032d60; margin: 0; font-size: 16px; font-weight: 500;">
                {icon} {message}
            </p>
        </div>
    """


def info_box_small(message, icon="ℹ️", margin_top="10px"):
    """
    Creates a smaller styled info box with Salesforce theme.
    
    Args:
        message: The text message to display
        icon: Optional emoji icon (default: ℹ️)
        margin_top: Top margin (default: 10px)
    
    Returns:
        HTML string for the small info box
    """
    return f"""
        <div style="background-color: white; padding: 15px; border-left: 4px solid #00A1E0; border-radius: 4px; margin-top: {margin_top};">
            <p style="color: #032d60; margin: 0; font-size: 16px; font-weight: 500;">
                {icon} {message}
            </p>
        </div>
    """


def feedback_box(content):
    """
    Creates a styled feedback box with Salesforce theme.
    
    Args:
        content: The feedback content to display (can include HTML)
    
    Returns:
        HTML string for the feedback box
    """
    return f"""
        <div style="background-color: white; padding: 25px; border: 2px solid #00A1E0; border-radius: 8px; margin-top: 20px; margin-bottom: 30px; box-shadow: 0 2px 8px rgba(0, 161, 224, 0.1);">
            <div style="color: #032d60;">
                {content}
            </div>
        </div>
    """

