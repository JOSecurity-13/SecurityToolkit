# This file contains the referenced modules in the main.py file
# libraries
import requests

# feedback colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# password strength analyzer
def lengthCheck(password: str) -> str:
    if len(password) < 8:
        print(bcolors.WARNING + "Your password is too short" + bcolors.ENDC)
    elif 14 <= len(password) <= 64:
        print(bcolors.OKCYAN + "Your password meets NIST guidelines for length!" + bcolors.ENDC)
    elif len(password) > 64:
        print(bcolors.WARNING + "Your password is too long" + bcolors.ENDC)

def specialCheck(password: str) -> str:

    checkDict = {
        "upperChar": False,
        "lowerChar": False,
        "numberChar": False,
        "specialChar": False
    }

    for char in password:
        if char.isupper():
            checkDict["upperChar"] = True
        elif char.islower():
            checkDict["lowerChar"] = True
        elif char.isdigit():
            checkDict["numberChar"] = True
        elif not char.isalnum():
            checkDict["specialChar"] = True

    if checkDict["upperChar"] and checkDict["lowerChar"] and checkDict["numberChar"] and checkDict["specialChar"]:
        print(bcolors.OKCYAN + "Your password has good entropy!" + bcolors.ENDC)
    else:
        print(bcolors.FAIL + "\n---------------\nYour password does not have strong entropy\n---------------\n" + bcolors.ENDC)
        for check, value in checkDict.items():
            if value == True:
                print(bcolors.OKGREEN + f"Your password has {check}" + bcolors.ENDC)
            else:
                print(bcolors.WARNING + f"Your password does not have {check}" + bcolors.ENDC)


# def breachCheck(password: str) -> str:

def passStrAnalyzer():

    print("\n---------Password Analyzer---------\n")
    print("l - length")
    print("e - entropy/complexity")
    print("a - check all available options")
    print("x - exit to menu\n\n----------------------------")


    strengthSelection = input("based on the above options what would you like to analyze your password for? ")
    if strengthSelection == "l":
        userPassword = str(input("Enter the password you would like to analyze "))
        lengthCheck(userPassword)
    elif strengthSelection == "e":
        userPassword = str(input("Enter the password you would like to analyze "))
        specialCheck(userPassword)
    elif strengthSelection == "a":
        userPassword = str(input("Enter the password you would like to analyze "))
        lengthCheck(userPassword)
        specialCheck(userPassword)
    elif strengthSelection == "x":
        print("\n Exiting Password Analyzer \n")






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


