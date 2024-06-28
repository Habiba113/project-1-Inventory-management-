## Define Inventory Dictionary
Inventory = {}
Total_sales = 0


def update_inventory(name,new_count):
        if name in Inventory:
            Inventory[name]['count']=new_count
            print("Inventory count of item '{}' updated to {}.".format(name,new_count))
        else:
            print("Item '{}'not found in inventory".format(name))
            
            
                 
        