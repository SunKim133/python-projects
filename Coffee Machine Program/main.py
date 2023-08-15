from CoffeeRecipe import MENU, resources

def calc_money(quarters, dimes, nickels, pennies):
    """Calculate the total money amount of coins"""
    money_value = quarters * .25 + dimes * .10 + nickels * 0.05 + pennies * 0.01
    return money_value

def resource_check(choice, current_resources):
    """Check if we have enough resources to make the drink"""
    for ingredient, amount in MENU[choice]['ingredients'].items():
        if current_resources[ingredient] < amount:
            print(f"Sorry, there's not enough {ingredient}.")
            return False
    return True

def calc_resources(current_resources, choice):
    """Calculate the amount of remained resources after the choice"""
    for ingredient, amount in MENU[choice]['ingredients'].items():
        current_resources[ingredient] -= amount

    return current_resources

def report(current_resources):
    """Print out the report page"""
    print(f"Water: {current_resources['water']}ml")
    print(f"Milk: {current_resources['milk']}ml")
    print(f"Coffee: {current_resources['coffee']}g")

def coffee_machine():
    is_machine_on = True
    current_resources = resources
    profit = 0
    while is_machine_on:
        choice = input("What would you like to drink? (espresso / latte / cappuccino): ").lower()
        if choice == 'report':
            report(current_resources)
            print(f"Money: ${profit:.2f}")
        elif choice == 'off':
            print("Turn off the machine. Bye!")
            is_machine_on = False
        elif choice in MENU:
            if resource_check(choice, current_resources):
                quarters = int(input("How many quarters? "))
                dimes = int(input("How many dimes? "))
                nickels = int(input("How many nickels? "))
                pennies = int(input("How many pennies? "))
                coins = calc_money(quarters = quarters, dimes = dimes, nickels = nickels, pennies = pennies)
                if coins <= MENU[choice]['cost']:
                    print("Sorry, that's not enough money. Money refunded.")
                else:
                    current_resources = calc_resources(current_resources, choice)
                    profit += MENU[choice]['cost']
                    print(f"Here is ${coins - MENU[choice]['cost']:.2f} in change.")
                    print(f"Here is your {choice}. Enjoy!")
        else:
            print("Invalid choice. Please select a valid drink.")


coffee_machine()