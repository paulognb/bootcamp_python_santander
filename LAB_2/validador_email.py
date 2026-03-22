email = input().lower().strip()

if "@" in email:
    dominio = email.split("@")[1]
    if (email.find("@")) > 0:
        if ("gmail.com" in dominio) or ("outlook.com" in dominio):
            print("E-mail válido")
        else:
            print("E-mail inválido")
    else:
            print("E-mail inválido")

else:
    print("E-mail inválido")