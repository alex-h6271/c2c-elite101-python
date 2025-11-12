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

def display_menu():
    print('\n**Super Epic Very Real Store Inventory System**')
    print("------------------------------------------")
    print('1. View Store Inventory')
    print('2. Add a Product')
    print('3. Remove a product')
    print('4. Exit')

def user_selection(login):
    
    user = int(input('Choose a service: '))

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
            print('Signing out of admin console...')
        print('Exiting program...')
    else:
        print('Invalid Input')

    return user, login

def display_inventory():
    print("\n**Super Epic Very Real Store Inventory**")
    for product in store_inventory:
        print("----------------------------")
        for key, value in product.items():
             print(f"{key}:{value}") 
    print("___________________________")
    
def admin_login(username, password):
    login = False
    username_guess = ' '
    
    password_guess = ' '
    print("\n**Super Epic Cool Store Admin Console**")
    print("---------------------------------------")
    
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
    type = str(input("Enter a type: "))
    while Valid == False:
        try:
            Valid = False
            price = float(input("Enter the price: "))
        except ValueError:
            print('Invalid Input')
            continue
        Valid = True
    Valid = False
    while Valid == False:
        try:
            total = int(input("Enter the amount: "))
        except total == 0:
            print('You can\'t add a product with 0 stock')
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
        PID = int(input('Input the Product ID: '))
    except ValueError:
        PID = 0
        
    for i, product in enumerate(store_inventory):         

        if store_inventory[i]["prod_Id"] == PID:

            to_delete_index = i  

            break
    if to_delete_index == -1:
        print('This item is not in the store inventory')
    store_inventory.pop(to_delete_index)
    print('Product removed succesfully')

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
while user != 4:
    display_menu()
    user, login = user_selection(login)


