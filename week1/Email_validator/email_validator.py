

def validate_email(email: str) -> bool:

    email = email.strip()

    if email.count("@") != 1 or email.count(" ") > 0 or email.startswith(".") or email.endswith("."):
        return False

    new_email  = email.split("@")
    login_part = new_email[0]
    domain_part = new_email[1]

    if len(login_part) == 0 or ".." in login_part:
        return False

    if "." not in domain_part or domain_part.startswith(".") or domain_part.endswith(".") or ".." in domain_part:
        return False
    return True


if __name__ == '__main__':
    #Valid Emails
    print(validate_email("madiyar20032009@gmail.com"))
    print(validate_email("ddd@blabla.work.com"))
    print(validate_email("1@gmail.com"))
    print(validate_email(" test@check.email.com "))
    print(validate_email("mail@mail.ru"))

    #Invalid Emails
    print(validate_email("mmm mail.ru"))
    print(validate_email("mmmm@ mail.ru"))
    print(validate_email(".mmmm@mail.ru"))
    print(validate_email("mmmm@@mail.ru"))
    print(validate_email("mmmm@mail..ru"))

    mail = input("Enter your email: ")
    if validate_email(mail):
        print("Email valid")
    else:
        print("Email not valid")
