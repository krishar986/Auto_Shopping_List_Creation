from selenium import webdriver
import smtplib
import time
import re
import datetime
dictionary_with_all_needed_item_values = {}
Inventory = open("Inventory_File.csv","r")
all_lines = Inventory.readlines()



def Print_List():
    list_of_lines = []
    email = smtplib.SMTP("smtp.gmail.com", 587)
    email.ehlo()
    email.starttls()
    email.login("tstmando@gmail.com","Mando@123")
    for key in dictionary_with_all_needed_item_values.keys():
        for item in dictionary_with_all_needed_item_values.values():
            item = item.split(",")
            line = item[0]+"\t"+key+"\t"+item[2]+"\t"+item[1]
            list_of_lines.append(line)

    list_of_lines = "\n".join(list_of_lines)         
    email.sendmail("tstmando@gmail.com", "rajivsharma76@gmail.com","Subject:Grocery List For"+datetime.datetime.now().strftime("%x")+"\n"+list_of_lines)
    email.quit()

    
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





def Available_Quantity_Calculation(Available_serving, Maximum_servings,servings_per_unit):
    quantity_in_servings = Maximum_servings - Available_serving
    Quantity = Available_serving/servings_per_unit
    return Quantity



def Webscraping_Prices(css_selector_fo_price, store_url):
    Chrome = webdriver.Chrome("/Users/krist/Desktop/Python/Course with Rahul Bahya/Inventory Management System Exercises/chromedriver")
    Chrome.get(store_url)
    price = Chrome.find_element_by_css_selector(css_selector_fo_price).text
    regex_to_remove_currency = re.compile(r'\d*\.\d{1,2}')
    y = regex_to_remove_currency.search(price)
    Chrome.close()
    return y.group()








add_item_or_update_or_print_list = input("Do you want to add items(enter 'a'), update inventory(enter 'u'), or print list('p'): ")

while add_item_or_update_or_print_list == "a" or add_item_or_update_or_print_list=="u"or add_item_or_update_or_print_list == "p":

    if add_item_or_update_or_print_list == "a":
        Adding_Items()
        all_lines = "\n".join(all_lines)
        Inventory.write(all_lines)



    elif add_item_or_update_or_print_list == "u":
        Update_Inventory_2()
        all_lines = "\n".join(all_lines)
        Inventory.write(all_lines)




    elif add_item_or_update_or_print_list == "p":
        list_of_prices = []
        dictionary_of_prices_and_stores = {}


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
                        dictionary_of_prices_and_stores[url[1]] = price
                        url_index += 1





                    list_of_prices.sort()
                    cheapest_price = list_of_prices[0]
                    stores = list(dictionary_of_prices_and_stores.keys())
                    prices = list(dictionary_of_prices_and_stores.values())
                    price_index= prices.index(str(cheapest_price))

                    store_with_cheapest_price = stores[price_index]
                    available_quantity = Available_Quantity_Calculation(int(item[2]),int(item[4]),int(item[5]))

                    quantity_needed = int(item[4])-available_quantity

                    dictionary_with_all_needed_item_values[store_with_cheapest_price] = item[0]+","+str(quantity_needed)+","+str(cheapest_price)
                    
                elif item[index] != "n":
                    price = Webscraping_Prices(item[8],item[6])

                    available_quantity = Available_Quantity_Calculation(int(item[2]),int(item[4]),int(item[5]))

                    quantity_needed = int(item[4])-available_quantity
                    dictionary_with_all_needed_item_values[item[6]] = item[0]+","+str(quantity_needed)+","+str(price)
        
    add_item_or_update_or_print_list = input("Do you want to add items(enter 'a'), update inventory(enter 'u'), or print list('p'): ")



Print_List()
