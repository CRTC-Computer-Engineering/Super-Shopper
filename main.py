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
aisle1 = ["mexican","international","gourmet","pasta","pizza dough","pizza sauce","rice"]
aisle2 = ["asain foods","bbq sauce","beans","mayo","mustard","relish","salad dressing","shortening","soups","canned vegetables"]
aisle3 = ["baking needs","baking","bake ware","cake mixes","cake decor","chocolate chips","coconut","cooking oil","flour","canned fruits","gravy","jams/jellies","pudding","salt","spices","stuffing","sugar","peanut butter"]
aisle4 = ["cereal","granola","Honey","oats","pancake mix"]
aisle5 = ["bread","cocoa","coffee","syrup","tea"]
aisle6 = ["juices","seltzer"]
aisle7 = ["cookies","crackers","soda"]
aisle8 = []
aisle9 = ["chips","seasonal"]
aisle10 = ["aluminum foil","freezer wrap","napkins","tissues"]
aisle11 = ["matches"]
aisle12 = ["house","mop","broom","cleaning"]
aisle13 = ["nuts"]
aisle14 = ["frozen foods"]
#This sets the items in the shopping list for comparison and sorting.
list_count = int(input("How many items are on your shopping list?: "))
shopping_list = []
shopping_list_final = []
for i in range(list_count):
    item = input("Enter item: ")
    shopping_list.append(item)

for item in aisle1:
    if item in shopping_list:
        shopping_list_final.append([item,"aisle1"])
for item in aisle2:
    if item in shopping_list:
        shopping_list_final.append([item,"aisle2"])
for item in aisle3:
    if item in shopping_list:
        shopping_list_final.append([item,"aisle3"])
for item in aisle4:
    if item in shopping_list:
        shopping_list_final.append([item,"aisle4"])
for item in aisle5:
    if item in shopping_list:
        shopping_list_final.append([item,"aisle5"])
for item in aisle6:
    if item in shopping_list:
        shopping_list_final.append([item,"aisle6"])
for item in aisle7:
    if item in shopping_list:
        shopping_list_final.append([item,"aisle7"])
for item in aisle8:
    if item in shopping_list:
        shopping_list_final.append([item,"aisle8"])
for item in aisle9:
    if item in shopping_list:
        shopping_list_final.append([item,"aisle9"])
for item in aisle10:
    if item in shopping_list:
        shopping_list_final.append([item,"aisle10"])
for item in aisle11:
    if item in shopping_list:
        shopping_list_final.append([item,"aisle11"])
for item in aisle12:
    if item in shopping_list:
        shopping_list_final.append([item,"aisle12"])
for item in aisle13:
    if item in shopping_list:
        shopping_list_final.append([item,"aisle13"])
for item in aisle14:
    if item in shopping_list:
        shopping_list_final.append([item,"aisle14"])
print(shopping_list_final)
