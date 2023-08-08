import json
import os
import uuid
scirpt_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(scirpt_directory)

inventory_path = './inventoy.json'
print('\n')
print('==== Welcome to Zesty Zomato: The Great Food Fiasco ====')



#load inventory

def loadInventory() :
    try :
        with open(inventory_path,'r') as file :
          return json.load(file)
    except FileNotFoundError :
        return []

inventory = loadInventory()['inventory']
order_inventory = loadInventory()['orders']

def saveInventory(inventory) :
    data = {'inventory': inventory,'orders' : order_inventory}
    with open (inventory_path,'w') as file :
        json.dump(data,file)

def saveOrderDetails(orders) :
    data = {'inventory': inventory,'orders' : orders}
    with open(inventory_path,'w') as file :
        json.dump(data,file)

#Add item 
def addItemToInventory():
    itemId = int(input('Enter Item ID: '))
    itemName= str(input('Enter the name of your new Item: '))
    itemPrice = int(input('Enter Price of the Item: '))
    availability = str(input('availability? (yes or no): '))

    if availability == 'yes' or 'no' :
        item = {
            "id":itemId,
            "name" :itemName ,
            "price":itemPrice ,
            "availabilty":availability
        }

        inventory.append(item)
        saveInventory(inventory)
        print(f"item added succesfull with of {itemId}")
        showOptions()
    else :
        print("Invalid Input ! Enter correct avaiblity as (yes or no)")
        addItemToInventory()
    


# Romove item
def removeItemFromInventory():
    idToRemove = int(input ('enter Id to be removed from Inventory:'))
    delinventory = [item for item in inventory if item['id'] != idToRemove ]
    saveInventory(delinventory)
    print ("item deleted successfully ")

# updater avaibiltity........
def updateAvailability():
    idToUpdate = int(input ('enter Id to be Updated from Inventory:'))
    availability= str(input('Enter Availability:(yes/no):' )).lower()
    
    if availability == 'yes' or availability == 'no' :
        for item in inventory :
            if item['id'] == idToUpdate :

                item["availabilty"]= availability
                saveInventory(inventory)
                print("item updated succesfully")
                showOptions()
                break

        print('enter valid id')
        showOptions()
    else :
        print("Invalid Input! Enter Correct Availablility")


#Update order status
def updateOrderStatus():
    orderId= input("enter order ID:")
    print("1.Pending")
    print("2.Preparing")
    print("3.Delivered")
    print("4.Cancelled")
    option = int(input('select an option to update (1-4): '))
    status = "Pending"
    if option == 1:
        status = "Pending"
    elif option == 2:
        status = "Preparing"
    elif option == 3:
        status = "Delivered"
    elif option == 4:
        status = "Cancelled"
    
    for item in order_inventory :
        if item['orderId'] == orderId :
            item.update({'status':status})
            saveOrderDetails(order_inventory)
            print ('order updated successfully!')
            showOptions()

#place order
def placeOrder():
    
    print('--------------------------')
    for item in inventory :
        if item["availabilty"] == "yes" :
            print('item id: ',item['id'])
            print(f"item name : {item['name']}")
            print(f'item price: {item["price"]}')
            print('--------------------------')

    id = input('enter product id you want to order : ')
    customername = input('Enter your name :')
    itemName=''
    itemPrice =''
    
    for item in inventory :
        if item['id'] == int(id) :
            itemName  = item['name']
            itemPrice = item['price']
            

    uniqid = uuid.uuid4()
    orderID= str(uniqid)

    orderDetails = {
        'orderId' : orderID,
        'customerName':customername,
        'productId': int (id),
        'itemName': itemName,
        'itemPrice' : itemPrice,
        'status':'pending'

    }

    order_inventory.append(orderDetails)
    saveOrderDetails(order_inventory)
    showOptions()



# View all orders

def viewAllOrders() :
    print(order_inventory)
    print('*=== All Order Details ==*')
    print('--------------------------')
    for item in order_inventory :
        print('order id : ',item['orderId'])
        print("customer name :",item['customerName'])
        print('item id: ',item['productId'])
        print(f"item name : {item['itemName']}")
        print(f'item price: {item["itemPrice"]}')
        print('status: ',item['status'])
        print('--------------------------')

    showOptions()

#Filter by status
def filterByStatus() :
    print("1.Pending")
    print("2.Preparing")
    print("3.Delivered")
    print("4.Cancelled")
    option = int(input('select an option to filter based on status (1-4): '))
    status = ""
    if option == 1:
        status = "Pending"
    elif option == 2:
        status = "Preparing"
    elif option == 3:
        status = "Delivered"
    elif option == 4:
        status = "Cancelled"
    
    print('--------------------------')
    
    for item in order_inventory :
        if item['status'] == status :
            print("customer name :",item['customerName'])
            print('item id: ',item['productId'])
            print(f"item name : {item['itemName']}")
            print(f'item price: {item["itemPrice"]}')
            print('status: ',item['status'])
            print('--------------------------')

    showOptions()


def selected_option(option) :
    if option == 1 :
        addItemToInventory()
    elif option == 2 :
        removeItemFromInventory()
    elif option == 3 :
        updateAvailability()
    elif option == 4 :
        placeOrder()
    elif option == 5 :
        updateOrderStatus()
    elif option == 6 :
        viewAllOrders()
    elif option == 7 :
        filterByStatus()
    elif option == 8 :
        print("\n")
        print("Thanks for visiting Zesty Zomato: The Great Food Fiasco ")
        exit()
        

def showOptions() :
    print('1.Add a new dish to the menu')
    print('2.Remove a dish from the menu')
    print('3.Update dish availability')
    print('4.Place a new order')
    print('5.Update order status')
    print('6.View all orders')
    print('7.Filter orders by status')
    print('8.Exit')
    print('\n')
    selectedOption = input('Please select an option (1-8): ')
   
    if selectedOption.isdigit() :
        if int(selectedOption) < 9 and int(selectedOption) > 0 :
            selected_option(int(selectedOption))
    else :
        print("Invalid Option")
        showOptions()


showOptions()





