## Define Inventory Dictionary
Inventory = {}
Total_sales = 0


def display_inventory():
        print('Current inventory')
        for items, details in Inventory.items():
            print(f'{items}: ${details['price']}*{details['count']}')
            print(f'Total sales:${Total_sales}') 
            
            
                 
        