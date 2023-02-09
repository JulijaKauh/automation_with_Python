import secrets
import string

def passwords(n):
    password = ""
    password_length = n

    letters = string.ascii_letters
    numbers = string.digits
    special_char = string.punctuation
    symbols = letters + numbers + special_char


    while True:
        for i in range(password_length):
            password += " ".join(secrets.choice(symbols))
        if len(password) <= n:
            break
    return "Your password is: {}".format(password)

print(passwords(23))
print(passwords(9))
print(passwords(10))
print(passwords(12))
