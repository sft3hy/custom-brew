import regex as re
import subprocess

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
    
def pretty_list(items):
    # Return an empty string if the list is empty
    if not items:
        return ""
    # If there's only one item, return it directly
    if len(items) == 1:
        return items[0]
    # If there are exactly two items, join them with ' and '
    if len(items) == 2:
        return ' and '.join(items)
    # For three or more items, join all but the last with commas, then add ', and ' before the last item
    return ', '.join(items[:-1]) + ', and ' + items[-1]