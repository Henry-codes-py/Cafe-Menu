

#create a list for cafe items on a menu
menu_items = ["coffee", "tea", "sandwich", "cake"]

#create a list for prices of cafe items
prices = [3.00, 2.50, 5.00, 4.00]

#create a list for quantities of cafe items
quantities = [2, 3, 1, 2]

#create a list for total prices of cafe items
total_prices = []

#loop through the menu items
for i in range(len(menu_items)):

  #calculate the total price for each item
  total_price = prices[i] * quantities[i]

  #add the total price to the list of total prices
  total_prices.append(total_price)

#print the list of total prices
print(total_prices)

print("Your total bill is: $", sum(total_prices))

user_selection = input("What would you like to order? ")

#check if the user's selection is in the menu items list
if user_selection in menu_items:

  #get the index of the user's selection in the menu items list
  item_index = menu_items.index(user_selection)

  #get the price of the user's selection from the prices list
  item_price = prices[item_index]

  #get the quantity of the user's selection from the quantities list
  item_quantity = quantities[item_index]

  #calculate the total price of the user's selection
  total_price = item_price * item_quantity

  #print the total price of the user's selection
  print("The total price of your order is: $", total_price)

else:

  #print an error message if the user's selection is not in the menu items list
  print("Sorry, we don't have that item on the menu.")