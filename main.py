import random import string
def generate_password(length=12, use_symbols=True, use_numbers=True, use_uppercase=True, use_lowercase=True) :
characters = ""
if use_symbols:
characters += string.punctuation
if use_numbers:
characters += string.digits
if use_uppercase:
characters +=
string.ascii_uppercase
if use_lowercase:
characters +=
string.ascii_lowercase
if not characters:
raise ValueError("At least one
character set must be selected.")
password =
• join (random. choice (characters) for - in range (length))
return password
if _name== " _main_":
print ("Generated Password:"
generate_password (length=16))
