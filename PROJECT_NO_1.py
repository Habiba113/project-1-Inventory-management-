## Define Inventory Dictionary
Inventory = {}
Total_sales = 0


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
 
     
            
            
                 
        