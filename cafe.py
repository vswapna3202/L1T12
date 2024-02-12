# This program has menu of all items in a cafe. It then has 2 dictionaries stock and menu for each item in
# the menu it gives the stock and price of the items in the respective dictionaries stock and price. 
# The total worth of all stocks of all items in the cafe is calculated and displayed
# Referred the below website for currency printing
# https://stackoverflow.com/questions/320929/currency-formatting-in-python

menu = [] # Declare an empty list variable menu

stock = {} # Declare an empty dictionary stock
price = {} # Declare an empty dicitonary price

while (True): #while true loop
    menu_item = input("Enter the menu items in your cafe (Type X to exit): ") #Get menu
    if (menu_item == "X"): #if X is entered break from loop       
            break        
    menu.append(menu_item)  #add menu_item to menu list

total_value = 0.0 # Declare total_value the total stock worth to be calculated as 0.0

for item in menu: #loop through each item in menu list
    stock[item] = int(input(f"\nEnter stock quantity for item {item.capitalize()}: ")) #get stock quantity of menu item   
    price[item] = float(input(f"Enter price for item {item.capitalize()}: ")) #get price of menu item
    total_value += stock[item] * price[item] #stock * price of each item is added to total_value in loop

# Print the total value of all stocks calculated above format it with currency and to 2 decimal digits
print(f"\nTotal Value of all the stocks in the cafe is: £{total_value:.2f}")
