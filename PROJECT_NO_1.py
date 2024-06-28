## Define Inventory Dictionary
Inventory = {}
Total_sales = 0


def change_price(name,new_price):
        if name in Inventory:
            Inventory[name]['price'] = new_price
            print('price of ' + name + ' changed to $' +str(new_price))
        else:
            print(name + "not found in inventory")
 
     
            
            
                 
        