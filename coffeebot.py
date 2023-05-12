# Define the main function of the coffee bot
def coffee_bot():
    print('Welcome to the cafe!')

    # Initialize variables
    order_drink = "y"
    drinks = []

    # Take orders until the user says no
    while order_drink == "y":
        size = get_size()
        drink_type = get_drink_type()

        # Combine size and drink type into a single string
        drink = f'{size} {drink_type}'
        print(f"Alright, that's a {drink}!")
        drinks.append(drink)

        while True:
            order_drink = input("Would you like another drink? (y/n) ")
            if order_drink in ("y", "n"):
                break

    # Print all ordered drinks
    print("Okay, so I have:")
    for drink in drinks:
        print(f"- {drink}")

    # Get the user's name and finalize the order
    name = input('Can I get your name please? \n> ')
    print(f'Thanks, {name}! Your order will be ready shortly.')

# Function to get the drink type from the user
def get_drink_type():
    res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')

    if res == 'a':
        return 'brewed coffee'
    elif res == 'b':
        return order_mocha()
    elif res == 'c':
        return order_latte()
    else:
        print_message()
        return get_drink_type()

# Function to handle mocha orders
def order_mocha():
    while True:
        res = input("Would you like to try our limited-edition peppermint mocha? \n[a] Sure! \n[b] Maybe next time! ")

        if res == "a":
            return "peppermint mocha"
        elif res == "b":
            return "mocha"

        print_message()

# Function to handle unrecognized inputs
def print_message():
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

# Function to get the drink size from the user
def get_size():
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')

    if res == 'a':
        return 'small'
    elif res == 'b':
        return 'medium'
    elif res == 'c':
        return 'large'
    else:
        print_message()
        return get_size()

# Function to handle latte orders
def order_latte():
    res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')

    if res == 'a':
        return 'latte'
    elif res == 'b':
        return 'non-fat latte'
    elif res == 'c':
        return 'soy latte'
    else:
        print_message()
        return order_latte()

# Start the coffee bot
coffee_bot()