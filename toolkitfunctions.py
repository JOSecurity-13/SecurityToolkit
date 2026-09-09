# This file contains the referenced modules in the main.py file
from main import bcolors


# password strength analyzer
def lengthCheck(password: str) -> str:
    if len(password) < 8:
        print(bcolors.WARNING + "Your password is too short" + bcolors.ENDC)
    elif 14 <= len(password) <= 64:
        print(bcolors.OKCYAN + "Your password meets NIST guidelines for length!" + bcolors.ENDC)
    elif len(password) > 64:
        print(bcolors.WARNING + "Your password is too long" + bcolors.ENDC)

def passStrAnalyzer(password: str) -> str:

    print("\n---------Password Analyzer---------\n")
    print("Entering no value will check for all ")
    print("l - length")
    print("c - casing")
    print("e - entropy/complexity")
    print("b - breach\n")

    strengthSelection = input("based on the above options what would you like to analyze your password for? ")
    if strengthSelection == "l":
        userPassword = input("Enter the password you would like to analyze ")
        lengthCheck(userPassword)
    elif strengthSelection == "c":
        pass
    elif strengthSelection == "e":
        pass
    elif strengthSelection == "b":
        pass
    elif strengthSelection == " ":
        pass


