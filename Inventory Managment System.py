from selenium import webdriver
import requests
Next_Step = input("Please enter 1 if you want to enter daily intake, enter 2 to get a list of all items you are running low on, enter 3 to update your inventory after coming home from shopping, enter 4 to add to you inventory: ")
#Csv should contain Item Name, Item Quantity, No. of Units, Servings per Unit, Treshold, Preffered Shop, Max Quantity, (Item Url, and Css_Selector, Store)
Inventory = open("Inventory_File.csv","a+")

dictionary_for_items_and_prices = {}




#this function will add items to the Inventory file, if the item exists that we will print a message that the item will already
def Validating_Numeric_Inputs(inputs):
    try:
        inputs = int(inputs)
    except ValueError:
        inputs = input("Please enter Natural Number: ")
        Validating_Numeric_Inputs(inputs)        
    if inputs < 0:
        inputs = input("Please enter Natural Numbers: ")
        Validating_Numeric_Inputs(inputs)
    inputs = str(inputs)
    return inputs




##    while inputs.isnumeric() != True and inputs > 0 and type(inputs) == int:
##        inputs = input("Please enter only Natural Number: ")
##    return inputs



def Open_Url(url):
    r = requests.get(url)
    while r.status_code == 404:
        url = input("Please enter a valid url: ")
    return url


def Go_to_Google_Maps(input_):
    Chrome =webdriver.Chrome("/Users/krist/Desktop/Python/Course with Rahul Bahya/Webscraping Exercises/chromedriver")
    Chrome.get("https://www.google.com/maps/search/"+input_)
    error_message = Chrome.find_elements_by_id("pane")
    error_string = "Google Maps can't find "+input_
    if error_string not in error_message[0].text:
        return input_
    else:
        input_ = input("Please enter a store that exists: ")
        input_ = Go_to_Google_Maps(input_)
        return input_
    
    

    

    
#Going to write using selenium
def searching_for_item(list_inputs,item_names):
   for i in Inventory:
        list_for_item_values=i.split(",")
        if list_for_item_values[0] == item_name:
            is_repeats = True
            for value in list_inputs:
                if value in list_for_item_values:
                    pass
                else:
                    is_repeats = False
                    print("Please go to Update to change your inventory: ")
                    break
            if is_repeats == True:
                print("Item already exists")
    return True
def Adding_Items():
#Input, Validate the Inputs, and Check if the Info repeats

        
        New_Item_Input = input("Enter the item name (please enter the full name of the item so you can exact lists when you are shopping): ")
        
        Quantity_Input = input("How many boxes or bags of this do you have: ")
        
        Serving_Input = input("How many available servings do you have, please enter in terms of your previous answer: ")

        Threshold_Input = input("How many Servings do you have left before you start to run out: ")

        Shop_Input = input("Please enter which shop you prefer to buy this item: ")
        




def Calculating_Available_Servings(amount_consumed, Quantity, servings_per_unit):
    total_quantity = Quantity * servings_per_unit
    amount_left = total_quantity - amount_consumed
    return amount_left




def Remove_Item(item_name):






def Quantity_Calculation(Available_serving, Maximum_servings):







def Cheapest_Price_Calculation(dictionary_of_all_item_and_prices):

list_of_all_prices = dictionary_of_all_prices.keys()
cheapest_price = list_of_all_prices.sort()[0]
return cheapest_price






def Webscraping_Prices(css_selector_of_price, store, store_url):






def Checking_if_Available_servings_below_Threshold():




    



def Print_List(item_name, store_name, cheapest_price, quantity_needed):






def Updating_Inventory(Amount_consumed, item_name):
