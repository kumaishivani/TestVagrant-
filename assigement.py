Leather_wallet=1100.00
umbrella=900.00
cigratte=200.00
Honey=100.00
print("*********************************NAME-Kumari Shivani********************************\n")
print("*********************************COLLEGE-LOVELY PROFESSIONAL UNIVERSITY********************************\n")
print("*********************************PASSING_YEAR-2023********************************\n")
print("*********************************EMAIL_id-shivaniyadav4972@gmail.com********************************")

print("Leather wallet:1100")
print("umbrella:900")
print("cigratte:200")
print("Honey:100")

while True:
    choice=input('\nChoose an item: Leather wallet, umberlla, cigratte, Honey\n')
    quantity=1
    rate=1100+198-64.9
    totalamount=(quantity*rate)
    if choice == 'Leather wallet':
        choice=input('Would you like to pick another order? y/n\n')
        if choice == 'y':
            choice=input('\nChoose an item: Leather wallet, umberlla, cigratte, Honey\n')
        else:
                print("total:",totalamount)
                print(" ")
    elif choice == 'umberlla':
        choice=input('Would you like to pick another order? y/n\n')
        quantity=2
        rate=900+108-50.4
        totalamount=(quantity*rate)
        if choice == 'y':
            choice=input('\nChoose an item: Leather wallet, umberlla, cigratte, Honey\n')
        else:
                print("Total cost:",totalamount)
                print(" ")
    elif choice == 'cigratte':
        choice=input('Would you like to pick another order? y/n\n')
        quantity=3
        rate=200+56
        totalamount=(quantity*rate)
        if choice == 'y':
            choice=input('\nChoose an item: Leather wallet, umberlla, cigratte, Honey\n')
        else:
                print("Total cost:",totalamount)
                print(" ")
    elif choice == 'Honey':
        choice=input('Would you like to pick another order? y/n\n')
        quantity=4
        rate=100
        totalamount=(quantity*rate)
        if choice == 'y':
            choice=input('\nChoose an item: Leather wallet, umberlla, cigratte, Honey\n')
        else:
                print("Total cost:",totalamount)
                print(" ")
    else:
        print("Error!")
    break
