def login(name, surname):
    username = "{}{}".format(name[0], surname).lower()
    email = username + "@" + "domain.com"
    return "{} {} your email is: {}.".format(name, surname, email)
