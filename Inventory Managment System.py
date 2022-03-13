Next_Step = input("Please enter 1 if you want to enter daily intake, enter 2 to get a list of all items you are running low on, enter 3 to update your inventory after coming home from shopping, enter 4 to add to you inventory: ")
Inventory = open("Inventory_File.txt","a+")

def Adding_Items():



def Calculating_Available_Servings(amount_consumed, Quantity):




def Remove_Item(item_name):






def Quantity_Calculation(Available_serving, Maximum_servings):




def Cheapest_Price_Calculation(list_of_all_prices):




def Webscraping_Prices(css_selector_of_price, store, store_url):



def Checking_if_Available_servings_below_Threshold():




    



def Print_List(item_name, store_name, cheapest_price, quantity_needed):






def Updating_Inventory(Amount_consumed, item_name):



#New Line

               


    
if Next_Step == "1":
    Breakfast = input("What did you eat for breakfast (enter full item name): ")
    Breakfast_Quantity = input("What type of breakfast did you eat a large(l), medium(m), small(s): ")
    if Breakfast_Quantity == "l":
        Breakfast_Quantity = 1.5
    if Breakfast_Quantity == "m":
        Breakfast_Quantity = 1
    if Breakfast_Quantity == "s":
        Breakfast_Quantity = 0.5
    
if Next_Step == "2":
    pass
if Next_Step == "3":
    pass
if Next_Step == "4":
    New_Item_Input = input("Enter the item name (please enter the full name of the item so you can exact lists when you are shopping): ")
    Inventory.write(New_Item_Input+", ")
    Quantity_Input = input("How many boxes or bags of this do you have: ")
    Inventory.write(Quantity_Input+", ")
    Serving_Input = input("How many available servings do you have, please enter in terms of your previous answer: ")
    Inventory.write(Serving_Input+", ")
    Threshold_Input = input("How many Servings do you have left before you start to run out: ")
    Inventory.write(Threshold_Input+", ")
    Shop_Input = input("Please enter which shop you prefer to buy this item: ")
    Inventory.write(Shop_Input+"\n")
    Inventory.flush()
