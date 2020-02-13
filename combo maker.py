from opggscraper import *
import random

fileInput = "scrape.txt"

while True:
    try:
        passwordInput1 = str(input("Password 1 to combo to: "))
        passwordInput2 = str(input("Password 2 to combo to: "))
        passwordInput3 = str(input("Password 3 to combo to: "))
        print("\n")

    except ValueError:  # check if entered password is not empty
        print("Please enter a password.", "\n")
        time.sleep(2)
        continue

    else:
        break

passwordBox = [passwordInput1, passwordInput2, passwordInput3]  # putting this into a list for later

try:
    with open(fileInput) as myFile:  # opening our file input
        lines = myFile.read().splitlines()  # read, then split at line breaks, giving us a list of lines to work with

except UnicodeDecodeError:  # catching if a string contains unicode that will not work with our chosen character encoding
    names_x2.remove() #if so, remove it from our list

with open(fileInput, 'w') as myFile:
    for line in lines:  # looping through our file
        print(line + ":" + random.choice(passwordBox), file=myFile)  # per username, randomly assign a password given through a list