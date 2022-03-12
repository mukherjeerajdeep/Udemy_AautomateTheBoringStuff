def user_choice():
    while True:
        choice = input("Please enter valid digit between 1-10:")

        if not choice.isdigit():
            print("Your input is either not a digit")
        else:
            if int(choice) in range(0, 11):
                return choice
            else:
                print("Your input is outside range")

print(user_choice())
