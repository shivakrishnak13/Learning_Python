import json
import os


inventory_path = "inventory.json"
# import os

# Get the directory of the script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Set the working directory to the script's directory
os.chdir(script_directory)




def load_inventory():
    try:
        with open(inventory_path, 'r') as file:
            data = json.load(file)
            return data.get('sanck_inventory', [])
    except FileNotFoundError:
        return []



inventory=[]
snack_menu=load_inventory()

selected_option = 0


def saveInventory(inventory_data) :
    data = {'sanck_inventory': inventory_data}
    with open(inventory_path,"w") as file :
         json.dump(data, file, indent=5)
    showFeatures()

def addSnack(snack_id,snack_name,price,availabilty) :
    snack_item = {
        "snackId": snack_id,
        "snackName" : snack_name,
        "price": price,
        "availability": availabilty
    }
    snack_menu.append(snack_item)
    saveInventory(snack_menu)

def additem():
    print("\nEnter details of new snack:")
    id = input('Snack_ID: ')
    name  =input ('Snack_Name:')
    price   = float (input ("Snack_Price:"))
    availability =(input("Availability:"))
    

    addSnack(id,name,price,availability)

def updateAvailability() :
    snackId = input("Enter Snack Id:")
    available= str((input("yes or no?")))
    for snack in snack_menu :
        if snack['snackId'] == str(snackId) :
            print(snack)
            snack['availability']=available
            print(f"Availability updated for snack ID {snackId}.")
            saveInventory(snack_menu)
    

def displayInventory() :
    
    print('-------------------------')
    for item in snack_menu :
        if item['availability'] == 'yes' :
            print("snackId:",item['snackId'])
            print("snackName:",item['snackName'])
            print("price:",item['price'])
            print("availability:",item['availability'])
        
            print('-------------------------')

    showFeatures()

def removeItem() :
    print('\nWhich Item do you want to delete?')
    delete = input('Do you want to Delete ? (yes/no)')
    if(delete == 'yes') :
        del_id = int(input('enter snack id :'))
        for snack in snack_menu:
            if snack['snackId'] == str(del_id):
                snack_menu.remove(snack)
                print(f"Snack with ID {del_id} removed from inventory.")
                saveInventory(snack_menu)
                return
    elif delete == 'no':
        showFeatures()
    else :
        print('Enter correct option (yes or no)')
        removeItem()
    print(f"Snack with ID {del_id} not found.")
    showFeatures()


def selectedOptions(option) :
    if option == "1" :
        displayInventory()
    elif option == "2" :
        additem()
    elif option == "3" :
        removeItem()
    elif option == '4' :
        updateAvailability()
    elif option == "5" :
        print('thanks for visiting')
        exit()

def showFeatures() :
    print("-------------------------------------")
    print("1.Display Snacks")
    print("2.Add a snack to the menu")
    print("3.Remove an item from the menu")
    print("4.update avaibilty of snack")
    print("5.Exit")
    option = input('Please select one Option :')
    selectedOptions(option)

showFeatures()
# print(snack_menu)