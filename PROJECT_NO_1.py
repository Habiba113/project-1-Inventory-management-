## Define Inventory Dictionary
Inventory = {}
Total_sales = 0


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
            
                 
        