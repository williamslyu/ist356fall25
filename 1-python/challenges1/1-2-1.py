

MAX_ATTEMPTS = 5
CORRECT_PASSWORD = "secret"

for attempt in range(MAX_ATTEMPTS):
    pwd = input("Enter password: ")

    if pwd == CORRECT_PASSWORD:
        print("access granted")
        break
    else:
        print("invalid password")

else:
    print("you are locked out")
