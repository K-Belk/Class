from terminaltables import AsciiTable
from classes.inventory import Inventory

cpv = Inventory()

main_menu = [
    ['Welcome to Code Platoon Video!'],
    ['1. View store video inventory'],
    ['2. View customer rented videos'],
    ['3. Add new customer'],
    ['4. Rent Video'],
    ['5. Return video'],
    ['6. Exit']
    ]
menu = AsciiTable(main_menu)
while True:
    print(menu.table)
    x = input('Please Make a selection\n')

    if x == '1':
        print(cpv.display_inventory())
        input('Enter any key to return to main menu\n')
    elif x == '2':
        print(cpv.display_customers())
        customer_id = input('Please chose a customer by id\n')
        print(cpv.customers[customer_id].display_customer())
        input('Enter any key to return to main menu\n')
    elif x == '3':
        cpv.add_customer()
        print('customer added')
    elif x == '4':
        print(cpv.display_customers())
        customer_id = input('Please chose a customer by id\n')
        print(cpv.display_inventory())
        video_id = input('Please select video to rent by id\n')
        if cpv.videos[video_id].copies_available > 0:
            if cpv.customers[customer_id].account_restrictions(cpv.videos[video_id]):
                cpv.rent_video(video_id, customer_id)
                print('rented')
            else:
                print('Restricted by account')
        else: print('Title not available')
    elif x == '5':
        print(cpv.display_customers())
        customer_id = input('Please chose a customer by id\n')
        if len(cpv.customers[customer_id].current_video_rentals) != 0:
            print(cpv.customers[customer_id].display_customer())
            while True:
                try:
                    video_index = int(input('Please select a title to return\n'))
                    if video_index > (len(cpv.customers[customer_id].current_video_rentals) - 1):
                        print('Please make a valid selection')
                        continue
                except:
                    print('Please enter an intiger')
                    continue
                break
            cpv.return_video(customer_id, video_index)
    elif x == '6':
        break
