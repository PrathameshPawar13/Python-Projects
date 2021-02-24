SECURE = (('P','P'),('r','R'),('a','@'),('t','T'),('h','|-|'),('a','@'),('m','|\/|'),('e','ϵ'),('s','$'),('h','|-|'))

def passwordfort(password):
    for a,b in SECURE:
        password=password.replace(a,b)

    return password

password=input("please enter the password here")
print(f"Your password is {passwordfort(password)}")

option=input("do you want upper case in your password? (y/n)")

if option=="y":
    print(f"Your password is {passwordfort(password)}")
else:
     print(f"Your password is {passwordfort(password.lower())}")
