Inventory = {}
Total_sales = 0

def main():
    print('<Welcome To Our Stock>')
    
## Create function "add items"
def add_items(name,price,count):
    Inventory[name] = {'price':price,'count':count}
    print('Item', name + " is added to inventory")
    def main():
            print('<Welcome To Our Stock>')
    while True:
        print('1: Add new items')
        choice = input('choose an option')
        if choice == 1:
            name = input('Enter item name')
            price = input('Enter item price')
            count = input('Enter item cost')
            add_items(name,price,count)
                
    ## Create function "buy_items"
def buy_item(name,quantity):
        if name in Inventory:
            if Inventory[name]['count'] >= quantity:
                Inventory[name]['count'] -=quantity
                total_price = Inventory[name]['price'] * quantity
                global Total_sales
                Total_sales += total_price
                print(f"{quantity} {name}(s) bough succesfully for ${total_price:.2f}.")
            else:
                print("Insufficient stock of '{}',".format(name))
        else:
            print("Item '{}' not found in invenory.".format(name))
            
    ## Update main function
def main():
        print('<Welcome To Our Stock>')
        while True:
            print('1: Add new item')
            print('2: Buy item')
            choice = input('Choose an option')
            if choice == '1':
                name = input('Enter item name:')
                price = float(input("Enter Item Price:"))
                count = int(input('Enter item Count:'))
                add_items(name,price,count)
            elif choice == '2':
                name = input('Enter item name:')
                new_price = float(input("Enter Item Price:"))
                change_price(name,new_price)
                
    ## Create function "change_price"
def change_price(name,new_price):
        if name in Inventory:
            Inventory[name]['price'] = new_price
            print('price of ' + name + ' changed to $' +str(new_price))
        else:
            print(name + "not found in inventory")
            
    ## Update main function
def main(name,new_price):
        print('<Welcome To Our Stock>')
        while True:
            print('1: Add new item')
            print('2: Buy item')
            print('3: Change_price')
            
            choice = input('Choose an option')
            if choice == '1':
                name = input('Enter item name:')
                price = float(input("Enter Item Price:"))
                count = int(input("Enter Item Count:"))
                add_items(name,price,count)
            elif choice == '2':
                name = input('Enter item name:')
                new_price = float(input("Enter New Price:"))
                change_price(name,new_price)
            elif choice == '3':
                name = input('Enter item name:')
                new_price = float(input('Enter new price:')) 
                change_price(name,new_price)
            
            
    ## Create function "Display_inventory"
def display_inventory():
        print('Current inventory')
        for items, details in Inventory.items():
            print(f'{items}: ${details['price']}*{details['count']}')
            print(f'Total sales:${Total_sales}') 
            
    ## Update main function
def main():
        print('<Welcome To Our Stock>')
        while True:
            print('1: Add new item')
            print('2: Buy item')
            print('3: Change_price')
            print('4: Display_inventory')
            choice = input('Choose an option')
            if choice == '1':
                name = input('Enter item name:')
                price = float(input("Enter Item Price:"))
                count = int(input("Enter Item Count:"))
                add_items(name,price,count)
            elif choice == '2':
                name = input("Enter item name to buy:")
                quantity = int(input("Enter quantity to buy:"))
                buy_item(name,quantity)
            elif choice == '3':
                name = input('Enter item name:')
                new_price = float(input('Enter new price:'))
                change_price(name,new_price)
            elif choice == '4':
                display_inventory()
            
            
    ## Create function "update_inventory"
def update_inventory(name,new_count):
        if name in Inventory:
            Inventory[name]['count']=new_count
            print("Inventory count of item '{}' updated to {}.".format(name,new_count))
        else:
            print("Item '{}'not found in inventory".format(name))
            
    ## Update main function
def main():
        print('< Welcome To Our Stock >')  
        while True:
            print('1: Add New Item')
            print('2: Buy An Item')
            print('3: Change Item Price')
            print('4: Display Inventory')
            print('5: Update Inventory Count')
            choice = input('^ Choose An Option:')
            if choice == '1':
                name = input('__ Enter Item Name:')
                price = float(input('__ Enter Item Price:'))
                count = int(input('__ Enter Item Count:'))
                add_items(name,price,count)
            elif choice == '2':
                name = input('__Enter Item Name To Buy:')
                quantity = int(input("__Enter Qunatity To Buy:"))
                buy_item(name,quantity)
            elif choice == '3':
                name = input('__Enter Item Name To Change Price:')
                new_price = float(input('__Enter New Price:'))
                change_price(name,new_price)
            elif choice == '4':
                display_inventory()
            elif choice == '5':
                name = input('__Enter Item Name To Update Count:')
                new_count = int(input('__Enter New Count:'))
                update_inventory(name,new_count)
                print(update_inventory)
main()
            