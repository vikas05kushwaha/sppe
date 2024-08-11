import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    print(email,"check emaildata")
    return re.match(pattern, email) is not None

def validate_mobile_number(mobile_number):
    pattern = r'^\d{10}$'
    return re.match(pattern, mobile_number) is not None

# checkemail=validate_email('vikas@gmail.com')
# print(checkemail)