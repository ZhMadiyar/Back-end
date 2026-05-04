

def validate_email(email: str) -> bool:

    email = email.strip()

    if email.count("@") != 1 or email.count(" ") > 0 or email.startswith(".") or email.endswith("."):
        print(email + " 1 false")
        return False

    new_email  = email.split("@")
    login_part = new_email[0]
    domain_part = new_email[1]

    if len(login_part) == 0 or ".." in login_part:
        print(email + " 2 false")
        return False

    if "." not in domain_part or domain_part.startswith(".") or domain_part.endswith(".") or ".." in domain_part:
        print(email + " 3 false")
        return False
    print(email + " true")
    return True


if __name__ == '__main__':
    #Valid Emails
    validate_email("madiyar20032009@gmail.com")
    validate_email("ddd@blabla.work.com")
    validate_email("1@gmail.com")
    validate_email(" test@check.email.com ")
    validate_email("mail@mail.ru")

    #Invalid Emails
    validate_email("mmm mail.ru")
    validate_email("mmmm@ mail.ru")
    validate_email(".mmmm@mail.ru")
    validate_email("mmmm@@mail.ru")
    validate_email("mmmm@mail..ru")

    mail = input("Enter your email: ")
    if validate_email(mail):
        print("Email valid")
    else:
        print("Email not valid")
