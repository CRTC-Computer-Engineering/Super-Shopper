import yaml
with open(r'data/stores.yaml') as file:
    fruits_list = yaml.safe_load(file)

    print(fruits_list)
    print(fruits_list["aisle"][1])

#This sets the store location, which has different items in different locations.
count = False
store = input("Where are you shopping?: ")
while count == False:
    #if store == "Hannaford" or store == "hannaford":
    if store.upper() == "hannaford".upper():
        store_items = []
        aisle_location = []
        count = True
    elif "sam".upper() in store.upper():
        store_items = []
        aisle_location = []
        count = True
    else:
        print ("Sorry, I don't recognize that store, try again.")
        store = input("Where are you shopping?: ")

#This sets the items in the shopping list for comparison and sorting.
list_count = int(input("How many items are on your shopping list?: "))
shopping_list = []
shopping_list_final = []
for i in range(list_count):
    item = input("Enter item: ")
    shopping_list.append(item)
for aisle in all aisle:      
    for item in shopping_list:
        if in shoping_list and aisle:
            shopping_list_final.append(item)
        else:
            None
print (shopping_list_final)