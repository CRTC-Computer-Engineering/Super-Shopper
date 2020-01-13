import yaml
import logging
#import wx

#app = wx.App()

#frame = wx.Frame(None, -1, "window Title")
#frame.Show()
#app.MainLoop()

fruits_list = []
logging.basicConfig(level=logging.INFO) # Set the logging level    

def find_aisle(search_item):
    for aisle, items in fruits_list.items(): #.iteritems() for python 2
        logging.debug("Currently looking at aisle " + str(aisle))
        try:
            for item in items:
                logging.debug("Currently checking item " + str(item).upper() + ", Looking for " + str(search_item).upper())
                if str(search_item).upper() == str(item).upper() :
                    logging.info("Found item " + str(item) + " in aisle " + str(aisle))
                    return aisle
        except:
            logging.warning("Error, no items in row: " + str(aisle))
    return None


with open(r'data/store1.yaml') as file:
    fruits_list = yaml.safe_load(file)

    #logging.debug(fruits_list)
    #logging.debug(fruits_list["aisle"]["1"])
    list_of_all_things_in_isle_1 = fruits_list["1"]

logging.info("Searched for item nuts and found item in: " + str(find_aisle("nuts")))

if __name__ == "_main__": # Run only if this is the main file
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

