def login(name, surname):
    username = "{}{}".format(name[0], surname).lower()
    email = username + "@" + "domain.com"
    return """{} {} your username is: {} and your password is: {}""".format(name, surname, username, email)



print(login("Sam", "Smitth"))
print(login("Katty", "Walter"))
print(login("Peter", "James"))
print(login("Dane", "Depp"))
print(login("Mary", "Cloud"))
