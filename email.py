def login(name, surname):
    username = "{}{}".format(name[0], surname).lower()
    email = username + "@" + "domain.com"
    return "{} {} your email is: {}.".format(name, surname, email)

print(login("Sam", "Smitth"))
print(login("Katty", "Walter"))
print(login("Peter", "James"))
print(login("Dane", "Depp"))
