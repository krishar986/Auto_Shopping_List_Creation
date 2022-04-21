#Inventory File Structure
#Item Name, Quantity, Available Servings, Threshold, Maximum Quantity, Servings Per Unit
#Url Information Structure
#Store, Url, Css_Selector



from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from prettytable import PrettyTable
from selenium import webdriver
import smtplib
import time
import re
from string import digits
import datetime
import requests





dictionary_with_all_needed_item_values = {}
Inventory = open("Inventory_File.csv","r")
all_lines = Inventory.readlines()
regex_to_remove_currency = re.compile(r'\d*\.\d{1,2}')





def Checking_if_Css_Selector_Exists(url,css_selector):
    Chrome = webdriver.Chrome("/Users/krist/Desktop/Python/Course with Rahul Bahya/Inventory Management System Exercises/chromedriver")

    Chrome.get(url)
    try:
        elements = Chrome.find_element_by_css_selector(css_selector).text
    except Exception:
        css_selector = "error"
    else:
        if len(regex_to_remove_currency.findall(elements)) == 0:
            css_selector = "error"
    return css_selector


def Open_Url(url):
#As an excercise convert to while loop
    Chrome = webdriver.Chrome("/Users/krist/Desktop/Python/Course with Rahul Bahya/Inventory Management System Exercises/chromedriver")
    try:
        if "https:" not in url:
            url = "https:"+url
        Chrome.get(url)
        time.sleep(5)
    except Exception:
        url = input("Please enter a valid url: ")
        url = Open_Url(url)
    error_string = "This site can’t be reached"
    error_message = Chrome.find_elements_by_id("main-message")
    if error_string in error_message:
        url = input("Please enter a valid url")
        url = Open_Url(url)
    return url


def Go_to_Google_Maps(input_):
    Chrome = webdriver.Chrome("/Users/krist/Desktop/Python/Course with Rahul Bahya/Inventory Management System Exercises/chromedriver")

    Chrome.get("https://www.google.com/maps/search/"+input_)
    error_message = Chrome.find_elements_by_id("pane")
    error_string = "Google Maps can't find "+input_
    if error_string not in error_message[0].text:
        return input_
    else:
        input_ = input("Please enter a store that exists: ")
        input_ = Go_to_Google_Maps(input_)
        return input_
    

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
    New_Item_Input = input("Enter the item name (please enter the full name of the item so you can exact lists when you are shopping): ")
    New_Item_Input = New_Item_Input.replace(",","_")
    Quantity_Input = input("How many boxes or bags of this do you have: ")
    Quantity_Input = Validating_Numeric_Inputs(Quantity_Input)
    
    Serving_Input = input("How many available servings do you have, please enter in terms of your previous answer: ")
    Serving_Input = Validating_Numeric_Inputs(Serving_Input)
    
    Threshold_Input = input("How many Servings do you have left before you start to run out: ")
    Threshold_Input = Validating_Numeric_Inputs(Threshold_Input)

    Max_Quantity = input("Please enter Max Quantity: ")
    Max_Quantity = Validating_Numeric_Inputs(Max_Quantity)

    Servings_per_Unit = input("Please enter how many servings are in one unit of this item: ")
    Servings_per_Unit = Validating_Numeric_Inputs(Servings_per_Unit)
    
    line = [New_Item_Input, Quantity_Input, Serving_Input, Threshold_Input, Max_Quantity, Servings_per_Unit]

    Shop_Input = input("Please enter which shop you prefer to buy this item(enter n if there is none): ")
    if Shop_Input != "n":
        Shop_Input = Go_to_Google_Maps(Shop_Input)
        Url_Input = input("Please enter the url for this item at that store: ")
        Url_Input = Open_Url(Url_Input)
        Css_Selector_Input = "error"
        while Css_Selector_Input == "error":
            Url_Input_y_n = input("Are you sure this is the correct url(y for yes)(n for no): ")
            if Url_Input_y_n == "n":
                Url_Input = input("Please enter the url for this item at that store: ")
                Css_Selector_Input = input("Please enter the css_selector for this item price at that url: ")
                Css_Selector_Input = Checking_if_Css_Selector_Exists(Url_Input, Css_Selector_Input)
            if Url_Input_y_n == "y":
                Css_Selector_Input = input("Please enter the css_selector for this item price at that url: ")
                Css_Selector_Input = Checking_if_Css_Selector_Exists(Url_Input, Css_Selector_Input)
        line.append(Shop_Input)
        line.append(Url_Input)
        line.append(Css_Selector_Input)
    else:
        line.append(Shop_Input)
        yes = True
    # 3 values for each store (URl,Store name, Css_selector), # of stores can vary from product to product ex: milk in 3 stores while matches are only available in one. Idea should factor all of this. 
        while yes == True:
            Store_Name_Input = input("Please enter the store name: ")
            Store_Name_Input = Go_to_Google_Maps(Store_Name_Input)
            Url_Input = input("Please enter the url: ")
            Url_Input = Open_Url(Url_Input)
            Css_Selector_Input = "error"
        while Css_Selector_Input == "error":
            Url_Input = input("Are you sure this is the correct url(y for yes)(n for no): ")
            if Url_Input == "n":
                Url_Input = input("Please enter the url for this item at that store: ")
                Css_Selector_Input = input("Please enter the css_selector for this item price at that url: ")
                Css_Selector_Input = Checking_if_Css_Selector_Exists(Url_Input, Css_Selector_Input)
            if Url_Input == "y":
                Css_Selector_Input = input("Please enter the css_selector for this item price at that url: ")
                Css_Selector_Input = Checking_if_Css_Selector_Exists(Url_Input, Css_Selector_Input)
            Store_Info = ";".join([Url_Input, Store_Name_Input, Css_selector_Input])
            line.append(Store_Info)
            asking_for_inputs = input("Do you want to enter store info(y for yes, anything else for no): ")
            if asking_for_inputs != "y":
                yes = False
    str_line = ",".join(line)
    all_lines.append(str_line)


def Calculating_Available_Servings(amount_consumed, Quantity, servings_per_unit):
    total_quantity = Quantity * servings_per_unit
    amount_left = total_quantity - amount_consumed
    return amount_left


def Available_Quantity_Calculation(Available_serving, Maximum_servings,servings_per_unit):
    quantity_in_servings = Maximum_servings - Available_servings
    Quantity = quantity_in_servings/servings_per_unit
    return Quantity
    

def Updating_Inventory_2():
    add_or_update = input("Do yo want to add items(enter 'a') to your inventory or update(enter 'u') your inventory, or if you want to change the url info then enter url: ")
    if add_or_update == "u":
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
            index_input = input("Please enter 1 for Item name, 2 for Quantity, 3 for Servings per Unit, 4 for Max Quantity, 5 Available Servings, 6 Max Quantity, 7 for Threshold, 8 for Url Information: ")
            index_input = Validating_Numeric_Inputs(index_input)
            index_input = int(index_input)
            result_list = result.split(",")
            while index_input > 8:
                index_input = int(input("Please enter 1 for Item name, 2 for Quantity, 3 for Servings per Unit, 4 for Max Quantity, 5 Available Servings, 6 Max Quantity, 7 for Threshold, 8 for Url Information: "))
            if index_input < 8:
                current_value_index = result_list[index_input - 1]
                index_input = Validating_Numeric_Inputs(index_input)
                index_input = int(index_input)
                updated_value = input("Please enter what you want the value to be: ")
                updated_result = result_list
                updated_result[current_value_index] = updated_value
            if index_input == 8:
            #TODO:Handle urls appending and updating
                current_value = input("Please enter the current value of the url: ")
                while current_value not in result:
                    current_value = input("Please enter the current value of the url: ")
                    current_value = Open_Url(current_value)
                new_url_value_input = input("Please enter what you want to change the url value to: ")
                updated_result = result_list
                current_url_index = updated_result.index(current_value)
                updated_result[current_url_index] = new_url_value_input
                new_css_selector_input = input("Please enter the new value of this urls css_selector: ")
                new_css_selector_input = Checking_if_Css_Selector_Exists(new_url_value_input,new_css_selector_input)
                updated_result[current_url_index + 1] = new_css_selector_input
                new_store_name_input = input("Please enter the store name of the entered url: ")
                updated_result[current_url_index - 1] = new_store_name_input
            all_lines[all_lines.index(result)] = ",".join(updated_result)
        else:
            print("None")
    elif add_or_update == "a":
        Adding_items()

    elif add_or_update == "url":
    
        item_exists = False
        while item_exists == False:
            Item_name = input("Pleae enter the name of the item you want to change the value for: ")
            for i in all_lines:
                line = i.split(",")
                if line[0] == Item_name:
                    item_exists = True
                    break
        while Item_name != "":
            Url_Input = input("Please enter the url: ")
            Url_Input = Open_Url(Url_Input)
            Store_Name_Input = input("Please enter the store name: ")
            Store_Name_Input = Go_to_Google_Maps(Store_Name_Input)
            Css_selector_Input = input("Please enter css_selector: ")
            Css_selector_Input = Checking_if_Css_Selector_Exists(Css_selector_Input)
            Store_Info = ",".join([Url_Input, Store_Name_Input, Css_selector_Input])
            line.append(Store_Info)
            all_lines.append(line)
            Item_name = input("Do you want to add more url information to this item, press enter if not: ")


def Print_List():
    html_table = """
                    <html>
                    <style>
                    table, th, td {
                      border:1px;
                      border-style: solid black;
                    }
                    </style>
                    <body>
                    <table style="width:100%">
                    <tr>                                
                    <th>ITEM NAME</th>
                    <th>RECOMMENDED STORE</th>
                    <th>PRICE</th>
                    <th>RECOMMENDED QUANTITY</th>
                    <th>ITEM NUMBER</th>
                    </tr>           
                    """
    list_of_lines = []
    email = smtplib.SMTP("smtp.gmail.com", 587)
    email.ehlo()
    email.starttls()
    email.login("tstmando@gmail.com","Mando@123")
    
    header = ["ITEM NAME", "RECOMMENDED STORE", "PRICE", "RECOMMENDED QUANTITY", "ITEM NUMBER"]
    dictionary_with_all_needed_item_values_sorted = sorted(dictionary_with_all_needed_item_values.items())
    translation_table = str.maketrans('', '', digits)
    for item in dictionary_with_all_needed_item_values_sorted:
        item_values = item[1].split(",")
        html_table = html_table+"<tr>"+"<td>"+item_values[0]+"</td>"+"<td>"+item[0].translate(translation_table)+"</td>"+"<td>"+item_values[2]+"</td>"+"<td>"+item_values[1]+"</td>"+"<td>"+str(dictionary_with_all_needed_item_values_sorted.index(item))+"</td>"+"</tr>"
        list_of_lines.extend([item_values[0], item[0].translate(translation_table), item_values[2], item_values[1], dictionary_with_all_needed_item_values_sorted.index(item)])
        
    html_table = html_table+"</table>"+"</body>"+"</html>"
                    
                      
##    list_of_lines = "\n".join(list_of_lines)
    message = MIMEMultipart()
    message.attach(MIMEText(html_table,"html"))
    table = message.as_string()
    email.sendmail("tstmando@gmail.com", "rajivsharma76@gmail.com","Subject:Grocery List For "+datetime.datetime.now().strftime("%x")+"\n"+table)
    email.quit()


def Validating_Numeric_Inputs(inputs):
    try:
        inputs = int(inputs)
    except ValueError:
        inputs = input("Please enter Natural Number: ")
        inputs = int(Validating_Numeric_Inputs(inputs))        
    if inputs < 0:
        inputs = input("Please enter Natural Numbers: ")
        inputs = int(Validating_Numeric_Inputs(inputs))
    inputs = str(inputs)
    return inputs


def Available_Quantity_Calculation(Available_serving, Maximum_servings,servings_per_unit):
    quantity_in_servings = Maximum_servings - Available_serving
    Quantity = quantity_in_servings/servings_per_unit
    return Quantity


def Webscraping_Prices(css_selector_for_price, store_url):
    Chrome = webdriver.Chrome("/Users/krist/Desktop/Python/Course with Rahul Bahya/Inventory Management System Exercises/chromedriver")
    Chrome.get(store_url)
    price = Chrome.find_element_by_css_selector(css_selector_for_price).text
    y = regex_to_remove_currency.search(price)
    Chrome.close()
    return y.group()










add_item_or_update_or_print_list = input("Do you want to add items(enter 'a'), update inventory(enter 'u'),update available servings(enter 'ua'), or print list('p'): ")

while add_item_or_update_or_print_list == "a" or add_item_or_update_or_print_list=="u"or add_item_or_update_or_print_list == "p" or add_item_or_update_or_print_list == "ua":

    if add_item_or_update_or_print_list == "a":
        Inventory.close()
        Inventory = open("Inventory_File.csv","w")
        Adding_Items()
        all_lines_str = "\n".join(all_lines)
        Inventory.write(all_lines_str)
        Inventory.flush()


    elif add_item_or_update_or_print_list == "u":
        Inventory.close()
        Inventory = open("Inventory_File.csv","w")
        Updating_Inventory_2()
        all_lines_str = "\n".join(all_lines)
        Inventory.write(all_lines_str)
        Inventory.flush()



    elif add_item_or_update_or_print_list == "p":
        list_of_prices = []
        dictionary_of_prices_and_stores = {}
        unique_id = 0

        for item in all_lines:
            item = item.split(",")
            index = 6
            url_index = 7
            url = item[url_index].split(";")
            last_index = item.index(item[-1])

            if int(item[2]) <= int(item[3]):
                if item[index] == "n":
                    while url_index <= last_index:
                        url = item[url_index].split(";")
                        price = Webscraping_Prices(url[2],url[0])
                        list_of_prices.append(float(price))
                        dictionary_of_prices_and_stores[price] = url[1]
                        url_index += 1





                    updated_list_of_prices = list_of_prices.sort()
                    cheapest_price = list_of_prices[0]
                    prices = list_of_prices
                    stores = list(dictionary_of_prices_and_stores.values())
                    price_index= prices.index(cheapest_price)

                    store_with_cheapest_price = stores[price_index]
                    available_quantity_in_servings = int(item[4])-int(item[2])
                    

                    quantity_needed = available_quantity_in_servings/int(item[5])

                    dictionary_with_all_needed_item_values[store_with_cheapest_price+str(unique_id)] = item[0]+","+str(quantity_needed)+","+str(cheapest_price)
                    unique_id += 1
                elif item[index] != "n":
                    price = Webscraping_Prices(item[8],item[7])

                    available_quantity_in_servings = int(item[4])-int(item[2])
                    quantity_needed = available_quantity_in_servings/int(item[5])

                    dictionary_with_all_needed_item_values[item[6] + str(unique_id)] = item[0]+","+str(quantity_needed)+","+str(price)
                    unique_id += 1
        Print_List()
    elif add_item_or_update_or_print_list == "ua":
        Inventory.close()
        Inventory = open("Inventory_File.csv","w")
        for item in all_lines:
            updated_item = item.split(",")
            servings_consumed = input("Please enter how much of "+updated_item[0]+" have you consumed: ")
            updated_item[2] = str(int(updated_item[2]) - int(servings_consumed))
            updated_item = ",".join(updated_item)
            all_lines[all_lines.index(item)] = updated_item
        all_lines_str = "\n".join(all_lines)
        Inventory.write(all_lines_str)
        Inventory.flush()
    add_item_or_update_or_print_list = input("Do you want to add items(enter 'a'), update inventory(enter 'u'),update available servings(enter 'ua'), or print list('p'): ")



Inventory.close()
