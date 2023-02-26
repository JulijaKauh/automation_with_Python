def login(name, surname):
    username = "{}{}".format(name[0], surname).lower()
    email = username + "@" + "domain.com"
    return """Hi {} {}, your username is {} and your email is {}""".format(name, surname, username, email)



print(login("Sam", "Smitth"))
print(login("Katty", "Walter"))
print(login("Peter", "James"))
print(login("Dane", "Depp"))
print(login("Mary", "Cloud"))

#!/usr/bin/env python3
def login():
    name = input("Name: ")
    surname = input("Surname: ")
    username = "{}{}".format(name[0], surname).lower()
    email = username + "@" + "domain.com"
    with open("user_email.txt", "a") as file:
        file.write("User: " + surname + " " + name + ". Login: " + username + ", email: " + email + "\n")
    print("Hi {} {}, your username is {} and your email is  {}""".format(name, surname, username, email))

login()
