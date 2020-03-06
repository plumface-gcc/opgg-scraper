from opggscraper import *
import random

fileInput = "scrape.txt"

numOfPasswords = int(input("How many passwords to combo to?: "))
#input1 = input("lol: ")
tempList = []

for i in range(numOfPasswords):
    tempList.append(input("Password to combo to: "))

try:
    with open(fileInput) as myFile:  # opening our file input
        lines = myFile.read().splitlines()  # read, then split at line breaks, giving us a list of lines to work with

except UnicodeDecodeError:  # catch if a string contains unicode that will not work with our chosen character encoding
    names_x2.remove()  # if so, remove it from our list

with open(fileInput, 'w') as myFile:
    for line in lines:  # looping through our file
        for word in tempList:
            print(line + ":" + word, file=myFile)  # per username, add password

""" loop thru username:username 
            
with open(fileInput, 'w') as myFile:
    for line in lines:  # looping through our file
        for word in line:
            print(line + ":" + line, file=myFile)
"""
print("Combo successfully completed.")
