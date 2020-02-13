from lxml import html
import requests, sys, locale, os, codecs, time

opggUrl = "https://na.op.gg/ranking/ajax2/ladders/start=" #where to start from
names_x2 = list()  # storing all data here

while True:
    try:
        myInput = int(input("What ladder rank do you want to start on?: "))
        myInput2 = int(input("How many accounts do you want to parse?: "))

    except ValueError:
        print("Please enter an integer.", "\n")
        time.sleep(2)
        continue

    else:
        break

for j in range(myInput, myInput + myInput2, 50):
    for i in [myInput]:
        destinationUrl = opggUrl + str(i)
        page = requests.get(destinationUrl)
        tree = html.fromstring(page.content)  # grabbing page html
        names_x1 = tree.xpath('//a[not(@target) and not(@onclick)]/text()')  # grabbing specific html content, this being the username
        names_x2.extend(names_x1)  # adding on to our list
        print("At position: ", [j], "\n")

with open("scrape.txt", "w", encoding="cp65001") as f:
    for item in names_x2:
        f.write("%s\n" % item)  # writing to txt file
        
print("\n")
print(len(names_x2), "names parsed.")
print("\n")
print("All data passed to text file successfully.", "\n\n\n")
time.sleep(2)
