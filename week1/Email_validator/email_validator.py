

def validate_email(email: str) -> bool:
    if email.count("@") != 1 or email.count(" ") >= 1 :
        return False
    else:
        return True




if __name__ == '__main__':
    print(validate_email("madiyar20032009@gmail.com"))
    print(validate_email("mmm mail.ru"))
    print(validate_email("mm mm@mail.ru"))


    mail = str(input("Enter your email: "))
    if validate_email(mail):
        print("Email valid")
    else:
        print("Email not valid")





