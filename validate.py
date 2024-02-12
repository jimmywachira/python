import re
email = input("whats your emai?").strip()

if re.search(r".+@.+\.com", email):
    print("valid")
else:
    print("invalid")


""""
re library regular expressions
if re.search(r".+@.+\.com", email): (raw expression -r)

email = input("whats your emai?").strip()

username, domain = email.split("@")

if username and "." in domain:
    print("valid")
else:
    print("invalid")    



"""