# This file contains the referenced modules in the main.py file


# password strength analyzer
def lengthCheck(password: str) -> str:
    if len(password) < 8:
        print(bcolors.WARNING + "Your password is too short" + bcolors.ENDC)
    elif 14 <= len(password) <= 64:
        print(bcolors.OKCYAN + "Your password meets NIST guidelines for length!" + bcolors.ENDC)
    elif len(password) > 64:
        print(bcolors.WARNING + "Your password is too long" + bcolors.ENDC)


    print("\n---------Password Analyzer---------\n")
    print("l - length")
    print("e - entropy/complexity")

    strengthSelection = input("based on the above options what would you like to analyze your password for? ")
    if strengthSelection == "l":
        lengthCheck(userPassword)
    elif strengthSelection == "e":


