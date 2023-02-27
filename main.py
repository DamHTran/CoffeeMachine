MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resources_sufficient(drink_input):
    # could compare drink with resource by looping each ingredient
    if drink_input == 'espresso':
        if MENU["espresso"]['ingredients']['water'] > resources['water']:
            print("Sorry there is not enough water")
        elif MENU["espresso"]['ingredients']['coffee'] > resources['coffee']:
            print("Sorry there is not enough coffee")
        else:
            return True
    elif drink_input == 'latte':
        if MENU["latte"]['ingredients']['water'] > resources['water']:
            print("Sorry there is not enough water")
        elif MENU["latte"]['ingredients']['milk'] > resources['milk']:
            print("Sorry there is not enough milk")
        elif MENU["latte"]['ingredients']['coffee'] > resources['coffee']:
            print("Sorry there is not enough coffee")
        else:
            return True
    elif drink_input == 'cappuccino':
        if MENU["cappuccino"]['ingredients']['water'] > resources['water']:
            print("Sorry there is not enough water")
        elif MENU["cappuccino"]['ingredients']['milk'] > resources['milk']:
            print("Sorry there is not enough milk")
        elif MENU["cappuccino"]['ingredients']['coffee'] > resources['coffee']:
            print("Sorry there is not enough coffee")
        else:
            return True


is_on = True
profit = 0

# TODO: 1. Asking drinks from user
while is_on:
    drink = input('What would you like? (espresso/latte/cappuccino): ')
# TODO: 2. Print report
    if drink == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${profit}')
    elif drink == 'off':
        is_on = False
    elif drink in ('espresso', 'latte', 'cappuccino'):
        # TODO: 3. Check resources sufficient
        # check resources sufficient
        if is_resources_sufficient(drink):
            # TODO: 4. Process coins
            print('Please insert coins.')
            quarters = int(input('how many quarters?: '))
            dimes = int(input('how many dimes?: '))
            nickles = int(input('how many nickles?: '))
            pennies = int(input('how many pennies?: '))
            total = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
            profit += MENU[drink]['cost']
            # TODO: 5. Check transaction successful
            if total > MENU[drink]['cost']:
                change = round(total - MENU[drink]['cost'], 2)
                print(f'Here is ${change} in change')
                # TODO: 6. Make coffee
                print(f'Here is your {drink}. Enjoy!')
                # TODO: 7. Update resource
                if drink in ('latte', 'cappuccino'):
                    resources['water'] -= MENU[drink]['ingredients']['water']
                    resources['milk'] -= MENU[drink]['ingredients']['milk']
                    resources['coffee'] -= MENU[drink]['ingredients']['coffee']
                else:
                    resources['water'] -= MENU[drink]['ingredients']['water']
                    resources['coffee'] -= MENU[drink]['ingredients']['coffee']
            else:
                print("Sorry that's not enough money. Money refunded")
                is_on = False

        else:
            is_on = False
    else:
        print('Invalid drink.')



































