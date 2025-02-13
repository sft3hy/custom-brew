import regex as re

def validate_email(email):
    """
    Validates an email address.
    Args:
        email (str): The email address to validate.
    Returns:
        bool: True if the email is valid, False otherwise.
    """
    # Regular expression for validating an Email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # Compile the ReGex
    pattern = re.compile(regex)
    # If the string is empty
    if email is None:
        return False
    # Matching the regex to the email
    if re.search(pattern, email):
        return True
    else:
        return False
    
