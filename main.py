#This sets the store location, which has different items in different locations.
count = False
store = input("Where are you shopping?: ")
while count == False:
    if store == "Hannaford" or store == "hannaford":
        store_items = []
        aisle_location = []
        count = True
    elif store == "Sam's" or store == "sam's" or store == "Sams" or store == "sams":
        store_items = []
        aisle_location = []
        count = True
    else:
        print ("Sorry, I don't recognize that store, try again.")
        store = input("Where are you shopping?: ")

#This sets the items in the shopping list for comparison and sorting.
list_count = int(input("How many items are on your shopping list?: "))
shopping_list = []
for i in range(list_count):
    item = input("Enter item: ")
    shopping_list.append(item)
        