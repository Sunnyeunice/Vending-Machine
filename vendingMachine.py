

import math
# global variables
TOONIES = 5
LOONIES = 5
QUARTERS = 20
DIMES = 30
NICKLES = 40

def display_welcome_menu():
    '''
    (none)-> none
    Displays the welcoming message and available options to the customer
    
    >>> display_welcome_menu()
    Welcome to the COMP 202 virtual Vending Machine.
    Here are your options:
    1. Candy bar $2.95
    2. Cookies $3.90 
    3. Soda $4.00
    4. Chips $3.90
    5. No snacks for me today!
    '''
    print("Welcome to the COMP 202 virtual Vending Machine.")
    print("Here are your options:")
    print("1. Candy bar $2.95")
    print("2. Cookies $3.90 ")
    print("3. Soda $4.00")
    print("4. Chips $3.90")
    print("5. No snacks for me today!")


def get_snack_price(choice):
    '''
    (int) -> int
    Returns price in cents for the choice of snack chosen from the menu
    
    >>> get_snack_price(1)
    295
    >>> get_snack_price(7)
    0
    >>> get_snack_price(3)
    400
    >>> get_snack_price(100)
    0
    '''
    # the price of chosen item is in cents
    if choice == 1:
        return 295
    elif choice == 2:
        return 390
    elif choice == 3:
        return 400
    elif choice == 4:
        return 390
    else:
        return 0

    
def get_num_of_coins(cost, value,  quantity):
    '''
    (int,int,int) -> int
    Returns maximum number of coins of given value to achieve target amount
    
    >>> get_num_of_coins(1200, 89, 6)
    6
    >>> get_num_of_coins(900, 100, 3)
    3
    >>> get_num_of_coins(50, 5, 2)
    2
    >>> get_num_of_coins(550, 200, 4)
    2
    '''
    # calculates max. number of coins by dividing cost by value
    coins = cost // value
    if coins > quantity:
        return quantity
    else:
        return coins


def compute_and_display_change(change):
    '''
    (int) -> bool
    Computes the most exact change by returning True or False accordingly
    
    
    >>> compute_and_display_change(590)
    Here is your change:
     toonies x  2
     loonies x  1
     quarter x  3
     dimes x  1
     nickles x  1
    True
    >>> compute_and_display_change(3)
    False
    >>> compute_and_display_change(5000)
    False
    >>> compute_and_display_change(100)
    Here is your change:
     toonies x  0
     loonies x  1
     quarter x  0
     dimes x  0
     nickles x  0
    True
    '''
    
    toonies = get_num_of_coins(change, 200, TOONIES)
    # only gives a max of 5 toonies; the rest converted to loonies
    change = change - (200 * toonies)
    loonies = get_num_of_coins(change, 100, LOONIES)
    # only gives a max of 5 loonies; the rest converted to quarters
    change = change - (100 * loonies)
    quarters = get_num_of_coins(change, 25, QUARTERS)
    # only gives a max of 20 quarters; the rest converted to dimes
    change = change - (25 * quarters)
    dimes = get_num_of_coins(change, 10, DIMES)
    # only gives a max of 30 dimes; the rest converted to nickles
    change = change - (10 * dimes)
    nickles = get_num_of_coins(change, 5, NICKLES)
    # only gives a max of 40 nickles.
    change = change - (5 * nickles)
    
    if change == 0: # the machine has enough coins to make the change
        print("Here is your change:")
        print(" toonies x ", toonies)
        print(" loonies x ", loonies)
        print(" quarter x ", quarters)
        print(" dimes x ", dimes)
        print(" nickles x ", nickles)
        return True 
    else: # the machine does not have enough coins to make the change
        return False

print(compute_and_display_change(40))

def operate_machine():
    '''
    (none) -> none
    Performs all the above tasks in the given order
    Retrieves some input from the user
    Computes and then displays various output as specified
    
    >>> operate_machine()
    Welcome to the COMP 202 virtual Vending Machine.
    Here are your options:
    1. Candy bar $2.95
    2. Cookies $3.90 
    3. Soda $4.00
    4. Chips $3.90
    5. No snacks for me today!
    Please select your choice: 5
    My snacks make you glow!! I hope you come back soon!
    >>> operate_machine()
    Welcome to the COMP 202 virtual Vending Machine.
    Here are your options:
    1. Candy bar $2.95
    2. Cookies $3.90 
    3. Soda $4.00
    4. Chips $3.90
    5. No snacks for me today!
    Please select your choice: 4
    The item of your choice costs 390 cents
    Enter your money : $30
    You inserted 3000 cents
    Your change is 2610 cents
    Sorry, there's not enough coins for your change. Next time!
    Welcome to the COMP 202 virtual Vending Machine.
    >>> operate_machine()
    Here are your options:
    1. Candy bar $2.95
    2. Cookies $3.90 
    3. Soda $4.00
    4. Chips $3.90
    5. No snacks for me today!
    Please select your choice: 2
    The item of your choice costs 390 cents
    Enter your money : $12
    You inserted 1200 cents
    Your change is 810 cents
    Here is your change:
     toonies x  4
     loonies x  0
     quarter x  0
     dimes x  1
     nickles x  0
    It was a pleasure doing business with you. See you soon!
    >>> operate_machine()
    Welcome to the COMP 202 virtual Vending Machine.
    Here are your options:
    1. Candy bar $2.95
    2. Cookies $3.90 
    3. Soda $4.00
    4. Chips $3.90
    5. No snacks for me today!
    Please select your choice: 3
    The item of your choice costs 400 cents
    Enter your money : $7.33378
    You inserted 734 cents
    We do not accept pennies. Come by another time!
    
    '''
    display_welcome_menu()
    choice = int(input("Please select your choice: "))
    m = "The item of your choice costs"
    r = "cents"
    
    if choice == 5:
        print("My snacks make you glow!! I hope you come back soon!") 
        return # terminates the execution
    # the following elif statements give the price for chosen item in cents 
  
    
    elif choice == 1:
        print(m, " 295", r)
        cost = 295
    elif choice == 2:
        print(m, "390", r)
        cost=390
    elif choice == 3:
        print(m, "400", r)
        cost=400
    elif choice == 4:
        print(m, "390", r)
        cost=390
        
    cash = float(input("Enter your money : $"))
    amount = math.ceil(cash * 100) #rounds up to 2 decimal places
    print("You inserted", amount, r)
    
    if amount % 5 != 0: # amount is not a multiple of 5
        print("We do not accept pennies. Come by another time!")
        return #terminates the execution
    
    if amount < cost:
    # amount entered by user is not enough to puy chosen item
        print("Sorry, your money is not enough. Come by another time!")
        return # terminates the execution 
    print("Your change is",(amount-cost), r) # displays the change needed
    if compute_and_display_change(amount-cost): # order successfully processes
        print("It was a pleasure doing business with you. See you soon!")
    else: # not possible to provide the change needed
        print("Sorry, there's not enough coins for your change. Next time!")
operate_machine() # calls the function
    
    
    
    
    
    
    


