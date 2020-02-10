try:
    from progress.bar import ChargingBar
    from lxml import html
    import requests, sys, locale, os, codecs, time
except:
    print("You do not have the proper libraries installed. Check output for which ones you're missing.")
    time.sleep(5)
    sys.exit()

opggUrl = "https://na.op.gg/ranking/ajax2/ladders/start=" #where to start from
names_x2 = list() #storing all data in a list
myInput = int(input("What ladder rank do you want to start on?: "))
myInput2 = int(input("How many accounts do you want to parse?: "))

for i in range(myInput, myInput + myInput2, 50):
    for i in [myInput]:
        destinationUrl = opggUrl + str(i) 
        page = requests.get(destinationUrl)
        tree = html.fromstring(page.content) #grabbing page html
        names_x1 = tree.xpath('//a[not(@target) and not(@onclick)]/text()') #getting the xpath of a specific part of the page 
        names_x2.extend(names_x1)

#names_x2 = [x.encode("UTF-8") for x in names_x2]
        
bar = ChargingBar("Working..", max=myInput2)

try:
    with open("scrape.txt", "w", encoding="cp65001") as f:
        for item in names_x2:
            names_x2 = [w.replace("Â", "") for w in names_x2] #find in list, then replace with blank
            names_x2 = [w.replace("Ã", "ø") for w in names_x2] #same shit different day
            names_x2 = [w.replace("¸", "") for w in names_x2]
            names_x2 = [w.replace("Ë", "ˇ") for w in names_x2]
            names_x2 = [w.replace("Ä", "") for w in names_x2]
            names_x2 = [w.replace("\x87", "") for w in names_x2]
            names_x2 = [w.replace("\x99", "ę") for w in names_x2]
            names_x2 = [w.replace("ø¬", "ì") for w in names_x2]
            print("\n") 
            f.write("%s\n" % item) #writing to txt file
            bar.next()
except:
    print("You must have a text file named scrape.txt for this to pass data into.")
    time.sleep(5)
    sys.exit()

bar.finish()
        
print("\n")
print(len(names_x2), "names parsed.")
print("\n")
print("All data passed to text file successfully.")
