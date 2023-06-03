import re 

email_pattern = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

user_email = input("Enter your Email: ")

if re.search(email_pattern,user_email):
    print("Email is valid")
else:
    print("Email in Invalid")
