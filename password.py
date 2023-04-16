#!/usr/bin/env python3
import secrets
import string
import sys 

n = sys.argv[1]
n = int(n)

def passwords(n):
    password = ""
    password_length = n

    letters = string.ascii_letters
    numbers = string.digits
    special_char = string.punctuation
    symbols = letters + numbers 


    while True:
        for i in range(password_length-1):
            password += " ".join(secrets.choice(symbols))

        for z in range(1):
            password += " ".join(secrets.choice(special_char))

            if len(password) <= n:
                break
        return "Length of your password is {}. Your password is: {} ".format(len(password), password)

print(passwords(n))

#The secrets module provides access to the most secure source of randomness that your operating system provides.
#secrets.choice(sequence): Return a randomly chosen element from a non-empty sequence.
#alphabet = string.ascii_letters + string.digits + string.punctuation
#letters = string.ascii_letters
#numbers = string.digits
#special_characters = string.punctuation
#all = string.printable
