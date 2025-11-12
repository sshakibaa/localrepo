import re

email = input("what's your email? ")

if re.search (r"^\w+@(\w+\.)?\w+(\.edu|\.com)$",email,re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")