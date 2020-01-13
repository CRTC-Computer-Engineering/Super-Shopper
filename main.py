import yaml
#import wx

#app = wx.App()

#frame = wx.Frame(None, -1, "window Title")
#frame.Show()
#app.MainLoop()

fruits_list = []

def find_aisle(search_item):
    for aisle in fruits_list["aisle"]:
        for item in aisle:
            print(item)
            if search_item == item :
                return aisle
    return None


with open(r'data/stores.yaml') as file:
    fruits_list = yaml.safe_load(file)

    print(fruits_list)
    print(fruits_list["aisle"]["1"])
    list_of_all_things_in_isle_1 = fruits_list["aisle"]["1"]

print(find_aisle("beans"))

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

