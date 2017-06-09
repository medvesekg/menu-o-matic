print "Welcome to Menu-o-matic, an easy way to create your menu."
print "Add your first dish"
#Adding items to the menu
menuItems = []
itemNumber = 1
while True:
    itemName = raw_input("Enter the name of the dish: ")
    itemDescription = raw_input("Enter a description: ")
    itemPrice = raw_input("Enter a price: ")

    menuItem = {"name": itemName, "description": itemDescription, "price": itemPrice, "number": itemNumber}
    menuItems.append(menuItem)

    addMore = raw_input("Would you like to add another dish? (y/n)")
    if "n" in addMore:
        break
    itemNumber += 1


while True:
    print "There are ", len(menuItems), " items in your menu. Would you like to review your menu before saving it to a file?"
    userInput = raw_input("review/save/exit: ")
    if userInput == "exit":
        break
    #Reviewing the menu
    if userInput == "review":
        print "\n"
        for item in menuItems:
            print "Item number ", item["number"]
            print item["name"]
            print item["description"]
            print item["price"]
            print "\n"
    #Saving to a file
    elif userInput == "save":
        fileName = raw_input("What would you like to name your file? (you don't need to write the file extension) ")
        with open(fileName + ".txt", "w") as menuFile:
            menuFile.write("MENU \n\n")
            for item in menuItems:
                menuFile.write("Item number " + str(item["number"]) + "\n")
                menuFile.write(item["name"] + "\n")
                menuFile.write(item["description"] + "\n")
                menuFile.write(item["price"] + "\n\n")
        break


