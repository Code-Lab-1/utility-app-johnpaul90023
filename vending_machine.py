def vending_machine(): 
    print("VENDING MACHINE")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------")
    bank=int(input("Enter your money: ")) # where the money stores
    stock=print({'Pepsi':21 , 'Sprite':22 , 'Fanta':23, 'Mountain Dew':24, 'Water':25, 'Cheetos':26, 'Lays chips':27, 'Pringles': 28, 'Snickers':29, 'Kit-Kat':30})
    while bank > 0: # numbers greater than 0 can purchase an item until the remaining balance is 0 or below 0
        itemschosen = int(input("Choose your item, to cancel the transaction enter 1: ")) # input for the chosen item or bevarage
        if itemschosen == 1: # when needed to cancel the transaction or stop the transaction
            break
        if itemschosen == 21:
            bank -= 2.50
            print('You have purchased Pepsi for 2.50$, your remaining balance is {}'.format(bank))
            print("------------------------------------------------------------------------------------------------------------------------------------------------------")
        if itemschosen == 22:
            bank -= 2.50
            print('You have purchased Sprite for 2.50$, your remaining balance is {}'.format(bank))
            print("------------------------------------------------------------------------------------------------------------------------------------------------------")
        if itemschosen == 23:
            bank -= 2.50
            print('You have purchased Fanta for 2.50$, your remaining balance is {}'.format(bank))
            print("------------------------------------------------------------------------------------------------------------------------------------------------------")
        if itemschosen == 24:
            bank -= 2.50
            print('You have purchased Mountain Dew for 2.50$, your remaining balance is {}'.format(bank))
            print("------------------------------------------------------------------------------------------------------------------------------------------------------")
        if itemschosen == 25:
            bank -= 2.50
            print('You have purchased Water for 2.50$, your remaining balance is {}'.format(bank))
            print("------------------------------------------------------------------------------------------------------------------------------------------------------")
        if itemschosen == 26:
            bank -= 1
            print('You have purchased Cheetos for 1$,  your remaining balance is {}'.format(bank))
            print("------------------------------------------------------------------------------------------------------------------------------------------------------")
        if itemschosen == 27:
            bank -= 4.50
            print('You have purchased Lays chips for 4.50$, your remaining balance is {}'.format(bank))
            print("------------------------------------------------------------------------------------------------------------------------------------------------------")
        if itemschosen == 28:
            bank -= 3.50
            print('You have purchased Pringles for 3.50$, your remaining balance is {}'.format(bank))
            print("------------------------------------------------------------------------------------------------------------------------------------------------------")
        if itemschosen == 29:
            bank -= 2.50
            print('You have purchased Snickers for 2.50$,  your remaining balance is {}'.format(bank))
            print("------------------------------------------------------------------------------------------------------------------------------------------------------")
        if itemschosen == 30:
            bank -= 2
            print('You have purchased Kit-Kat for 2$, your remaining balance is {}'.format(bank))
            print("------------------------------------------------------------------------------------------------------------------------------------------------------")
        if bank < 1: #when bank is less than 1 it will stop the code
            print("You have insufficient balance, your remaining balance is {}".format(bank))
            print("------------------------------------------------------------------------------------------------------------------------------------------------------")
            break
vending_machine()



