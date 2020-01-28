import wx
import logging as log

list_count = 0

class Frame1(wx.Frame):
    def __init__(self): # Init here
        super().__init__(parent=None, title='Speedy Shopper') # title
        self.panel = wx.Panel(self) # To put widgets on
        self.txt_ctrl = wx.TextCtrl(self.panel, pos=(5, 45)) # Controool bgox
        self.txt_ctrl.SetValue("")
        wx.StaticText(self.panel, label="Are you Shopping at Hannford?", pos=(5, 20))
        config_btn = wx.Button(self.panel, label='Submit ', pos=(5, 70)) # button
        config_btn.Bind( wx.EVT_BUTTON, self.calc) # Binds the button, to the event EVT_ BUTON, witch calls self.calc
        self.Show()

    def calc(self, event):
        log.info("Checking..")
        if self.txt_ctrl.GetValue().upper() == "yes".upper():
            log.debug ("working")
            self.Hide()
            frame1.Show()
        else:
            self.Hide()

class Frame2(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Speedy Shopper')
        self.panel = wx.Panel(self)
        wx.StaticText(self.panel, label="How many items are you shopping for?", pos=(5, 20))
        self.txt_ctrl = wx.TextCtrl(self.panel, pos=(5, 45))
        config_btn1 = wx.Button(self.panel, label='Submit', pos=(5, 70))
        config_btn1.Bind( wx.EVT_BUTTON, self.calc)
    def calc(self, event):
        list_count = self.txt_ctrl.GetValue()
        print (list_count)
        self.Hide()
        frame2.Show()
class Frame3(wx.Frame):
    def __init__(self):
        delete_me = [("Jeff"), ("Pancakes"),("Four")]
        super().__init__(parent=None, title='Speedy Shopper')
        self.panel = wx.Panel(self)
        id = wx.NewIdRef()
        self.gui_list = wx.ListCtrl(self, id,
                                    style=wx.LC_REPORT|
                                    wx.SUNKEN_BORDER)
        self.gui_list.InsertColumn(0, "Ur mom")
        for item in delete_me:
            self.gui_list.SetItem(1, item) #THese args wrong
        #config_btn1.Bind( wx.EVT_BUTTON, self.calc)
    #    frame1.list_count


if __name__ == '__main__':
    log.basicConfig(level=log.DEBUG)# Sets global logging level to debug
    app = wx.App()
    frame = Frame1()
    frame1 = Frame2()
    frame2 = Frame3()
    app.MainLoop()



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
