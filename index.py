SECURE = (('s' ,'$' ),('and' , '&' ),('a' , '@' ),('o' , '0'), ('i' , '1'), ('m' , '*' ), ( 'd', '/'), ('f ',' -') )

def securePassword(password):
    try:
        for a,b in SECURE:
            password = password.replace(a,b)
    except:
        print("Some Error Occurred")
    return password
        

if __name__ == "__main__":
    password = input("Enter your password: ")
    secure_password = securePassword(password)
    print(f"Your Secure Password is {secure_password}")
