# import modules
from toolkitfunctions import *

# Menu
def menu():
    menu_options = ("p", "c", "l", "s", "q")

    # loop to keep program running
    while True:

        # block or menu options
        print("---- Menu ----")
        print("p - Password Strength Analyzer")
        print("c - Cipher Toolkit")
        print("l - Log Threat Scanner")
        print("s - Port/Subnet Helper")
        print("q - Quit\n")

        # take in user input
        user_input = input("Please select an option from above (p, c, l, s, q): ")

        if user_input in menu_options:
            if user_input == "p":
                passStrAnalyzer()
                continueCheck = input("Do you wanna continue? (y/n): ")
                if continueCheck == "y":
                    continue
                elif continueCheck == "n":
                    break
            elif user_input == "c":
                break
            elif user_input == "l":
                break
            elif user_input == "s":
                break
            elif user_input == "q":
                break

        else:
            print()
            print(bcolors.FAIL + "----------------------\n" + "OPTION NOT AVAILABLE" + "\n----------------------\n" + bcolors.ENDC)
            print()

if __name__ == "__main__":
    menu()