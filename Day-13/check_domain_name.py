domain_key = ["@gmail.com", "@mail.com", "@facebook.com", "@yahoo.com", "@apple.com", "@mail.com"]
chr_special = [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 58, 59, 60, 61, 62, 63, 91, 92, 93, 94,
               95, 96, 123, 124, 125, 126]


def checking_domain(e):
    check_name = "pass"
    check_domain = "fail"
    leng = len(e)
    for i in range(leng):
        if e[i] == '@':
            domain_name = e[0:i]
            domain_form = e[i:]
            for j in domain_name:
                for k in chr_special:
                    if k == ord(j):
                        check_name: str = "fail"
                        break
            for k in domain_key:
                if k == domain_form:
                    check_domain = "pass"
    if check_domain == "pass" and check_name == "pass":
        return "pass"
    else:
        return "fail"


if __name__ == '__main__':
    while True:
        get_mail: str = input("Enter your domain :> ")
        get_pass = checking_domain(get_mail)
        if get_pass == "pass":
            print("your domain is success!!!")
        else:
            print("your domain is fail!!!")
