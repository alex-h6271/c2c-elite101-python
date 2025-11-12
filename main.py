import random

store_inventory = [
  {'prod_Id': 4327, 'type': 'Shoes', 'price': 100.0, 'total': 20},
  {'prod_Id': 3915, 'type': 'Tshirts', 'price': 43.5, 'total': 32},
  {'prod_Id': 2119, 'type': 'Pants', 'price': 34.0, 'total': 19},
  {'prod_Id': 1194, 'type': 'Jumpers', 'price': 250.0, 'total': 5},  
  {'prod_Id': 1300, 'type': 'Blouse', 'price': 24.76, 'total': 3},
  {'prod_Id': 1118, 'type': 'Dress', 'price': 50.0, 'total': 10}, 
  {'prod_Id': 1664, 'type': 'Suits', 'price': 250, 'total': 5}
] 

username = 'Manager123'

password = '#ManagerSoCool456'

login = False
  
def display_menu(id, login):
    print('\n**Super Epic Very Real Store Inventory System**')
    print("------------------------------------------")
    if login == True:
        print(f'What can I assist you with, Manager?')
    else:
        print(f'What would you like to do, employee #{id}?')
    print('1. View Store Inventory')
    print('2. Add a Product')
    print('3. Remove a product')
    print('4. Exit')

def user_selection(login):
    
    user = int(input('Please choose a service: '))

    if user == 1:
        display_inventory()
    elif user == 2:
        if login == False:
            login = admin_login(username, password)
        add_new_product()
    elif user == 3:
        if login == False:
            login = admin_login(username, password)
        remove_product()
    elif user == 4:
        if login == True:
            print('Signing you out of the admin console...')
        print('Exiting program...')
    else:
        print('Oops! that is an invalid Input')

    return user, login

def display_inventory():
    print("\n**Super Epic Very Real Store Inventory**")
    print('Displaying store inventory…')
    for product in store_inventory:
        print("----------------------------")
        for key, value in product.items():
             print(f"{key}:{value}") 
    print("___________________________")

def employee_login():
    id = 0
    print('\n**Super Epic Very Real Store Inventory System**')
    print("------------------------------------------")
    print('Hello, it seems you are attempting to access the internal store inventory system, could you please lrovide your ID number?')
  
    while id == 0:
        try:
            id = int(input('Please enter your employee ID number: '))
        except ValueError:
            print('Oops! Seems like whatever you entered is invalid! Try again!')
            continue
    
    print(f'Valid ID number detected: Welcome employee #{id}!')
  
    return id
    
def admin_login(username, password):
    login = False
    username_guess = ' '
    
    password_guess = ' '
    print("\n**Super Epic Cool Store Admin Console**")
    print("---------------------------------------")
    print('It appears you are trying to access a function that requires administrative permissions, plese provide the required login information.')
    
    while username_guess != username and password_guess != password:
        username_guess = str(input('Enter the admin username: '))
        password_guess = str(input('Enter the password: '))
    print('Logging in...')
    login = True
    
    return login
    

def add_new_product():
    Valid = False
    print("\n **Adding A New Product To The Inventory**")
    print("------------------------------------")
    type = str(input("Please enter an item type: "))
    while Valid == False:
        try:
            Valid = False
            price = float(input("Please enter the price: "))
        except ValueError:
            print('Sorry, that is an invalid Input!')
            continue
        Valid = True
    Valid = False
    while Valid == False:
        try:
            total = int(input("Please enter the amount: "))
        except total == 0:
            print('Oops! You can\'t add a product with 0 stock!')
            continue
        Valid = True
    new_product = Product(type, price, total)
    store_inventory.append(new_product.features())

def remove_product():  

    to_delete_index = -1
    display_inventory()
    print("\n **Removing A Product From The Inventory**")
    print("------------------------------------")
    try:
        PID = int(input('Please input the Product ID of tbe requested item: '))
    except ValueError:
        PID = 0
        
    for i, product in enumerate(store_inventory):         

        if store_inventory[i]["prod_Id"] == PID:

            to_delete_index = i  

            break
    if to_delete_index == -1:
        print('Sorry, this item is currently not in the store inventory')
    store_inventory.pop(to_delete_index)
    print('The requested product has been removed succesfully')

class Product:
    def __init__(self, type, price, total):
        self.prod_Id = random.randint(1000,9999)
        self.type = type        
        self.price = price        
        self.total = total

    def features(self):
      return {"prod_Id":self.prod_Id,
              "type":self.type,
              "price":self.price,
              "total":self.total
             }

user = 0
id = employee_login()
while user != 4:
    display_menu(id, login)
    user, login = user_selection(login)


