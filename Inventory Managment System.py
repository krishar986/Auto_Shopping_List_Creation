from selenium import webdriver
import requests
Next_Step = input("Please enter 1 if you want to enter daily intake, enter 2 to get a list of all items you are running low on, enter 3 to update your inventory after coming home from shopping, enter 4 to add to you inventory: ")
#Csv should contain Item Name, Item Quantity, No. of Units, Servings per Unit, Treshold, Preffered Shop, Max Quantity, (Item Url, and Css_Selector, Store)
Inventory = open("Inventory_File.csv","w+")

dictionary_for_items_and_prices = {}
all_lines = Inventory.readlines()




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
    try:
        r = requests.get(url)
    except requests.exceptions.MissingSchema:
        url = input("Please enter a valid url: ")
        url = Open_Url(url)        
        if r.status_code == 404:
            url = input("Please enter a valid url: ")
            url = Open_Url(url)
        
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
                    return 1
                    pass
                else:
                    is_repeats = False
                    print("Please go to Update to change your inventory: ")
                    return 2
                    break
            if is_repeats == True:
                print("Item already exists")
                return 3



def Adding_Items():
#Input, Validate the Inputs, and Check if the Info repeats

        
        New_Item_Input = input("Enter the item name (please enter the full name of the item so you can exact lists when you are shopping): ")
        
        Quantity_Input = input("How many boxes or bags of this do you have: ")
        Quantity_Input = Validating_Numeric_Inputs(Quantity_Input)
        
        Serving_Input = input("How many available servings do you have, please enter in terms of your previous answer: ")
        Serving_Input = Validating_Numeric_Inputs(Serving_Input)
        
        Threshold_Input = input("How many Servings do you have left before you start to run out: ")
        Threshold_Input = Validating_Numeric_Inputs(Threshold_Input)

        Max_Quantity = input("Please enter Max Quantity: ")
        Max_Quantity = Validating_Numeric_Inputs(Max_Quantity)
        
        Shop_Input = input("Please enter which shop you prefer to buy this item: ")
        Shop_Input = Go_to_Google_Maps(Shop_Input)
        # 3 values for each store (URl,Store name, Css_selector), # of stores can vary from product to product ex: milk in 3 stores while matches are only available in one. Idea should factor all of this. 
        asking_if_
        while 
        Url_Input = input("Please enter the url 

        
        line = ",".join([New_Item_Input, Quantity_Input, Serving_Input, Threshold_Input, Max_Quantity, Shop_Input])
        all_lines.append(line)

def Calculating_Available_Servings(amount_consumed, Quantity, servings_per_unit):
    total_quantity = Quantity * servings_per_unit
    amount_left = total_quantity - amount_consumed
    return amount_left




def Remove_Item(item_name):
    for i in all_lines:
        list_item_info= i.split(",")
        if list_of_item_info[0] == item_name:
            all_lines.remove(i)





def Quantity_Calculation(Available_serving, Maximum_servings):







def Cheapest_Price_Calculation(dictionary_of_all_item_and_prices):

list_of_all_prices = dictionary_of_all_prices.keys()
cheapest_price = list_of_all_prices.sort()[0]
return cheapest_price






def Webscraping_Prices(css_selector_of_price, store, store_url):






def Checking_if_Available_servings_below_Threshold():




    



def Print_List(item_name, store_name, cheapest_price, quantity_needed):










def Updating_Inventory_2():
    for i in all_lines:
        print(i)
    item_name = input("Please enter the name of the item you want to update: ")
    result = None
    for i in all_lines:
        list_of_values = i.split(",")
        if item_name in list_of_values[0]:
            result = i
    if result != None:
        print(result)
        index_input = input("Please enter 1 for Item name, 2 for Quantity, 3 for Servings per Unit, 4 for Max Quantity, 5 Available Servings, 6 Max Quantity, 7 for Threshold, 8 for Url: ")
        Validating_Numeric_Inputs(index_input)
        index_input = int(index_input)
        result_list = result.split(",")
        while index_input > 8:
            index_input = input("Please enter 1 for Item name, 2 for Quantity, 3 for Servings per Unit, 4 for Max Quantity, 5 Available Servings, 6 Max Quantity, 7 for Threshold, 8 for Url: ")
            Validating_Numeric_Inputs(index_input)
            index_input = int(index_input)
        if index_input < 8:
            current_value = result_list[index_input - 1]
        if index_input == 8:
            current_value = input("Please enter the current value of the url: ")
            while current_value not in result:
                current_value = input("Please enter the current value of the url: ")
                Open_Url(current_value)
        new_value_input = input("Please enter what you want to change the value to: ")
        updated_result = result.replace(current_value,new_value_input)
        all_lines[all_lines.index(result)] = updated_result
    else:
        print("None")

        
##def Updating_Inventory_2():
##
##
##"""
##Identify which line's value needs to be update
##Identify what value of the line need to be updated
##"""
##    all_lines = Inventory.readlines()
##    for i in all_lines:
##        print(i)
##    item_name = input("Please enter the name of the item you want to update: ")
##    for i in all_lines:
##        list_of_values = i.split(",")
##        if list_of_values[0] == item_name:
##            current_value = input("Please enter the the current value of the value you want to change: ")
##            
##            if current_value in list_of_values:
##                if type(current_value) == int:
##                    current_value = Validating_Numeric_Inputs(current_value)
##                    
##                new_value = input("Please enter what you want to replace the value with: ")
##                i.replace(current_value, new_value)
##            else:
##                current_value = input("Please enter something in the list: ")
##                Updating_Inventory_2()
##        else:
##            item_name = input("Please enter an item name existing in the Inventory: ")
##                
##                
