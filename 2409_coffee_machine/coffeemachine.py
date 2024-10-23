from logo import LOGO

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
    },
}

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0, "intake": 0}
CURRENCY = "$"

COIN_VALUES = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}


# Function to take input about User's Choice
def take_input():
    coffe_type = input("What would you like? espresso/latte/cappuccino ").lower()
    return coffe_type


# Print Report of Coffee
def report_resources():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}ml")
    print(f"Money: {resources["money"]}ml")


# Function to Ask Money and Return Total
def insert_money():
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    money = (
        COIN_VALUES["quarters"] * quarters
        + COIN_VALUES["dimes"] * dimes
        + COIN_VALUES["nickles"] * nickles
        + COIN_VALUES["pennies"] * pennies
    )
    return money


def transaction(cost, paid):
    cost = float(cost)
    paid = float(paid)
    if paid < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif paid == cost:
        resources["money"] += paid
        print("Thank you for your payment. Enjoy your drink!")
        return True
    elif paid > cost:
        change = paid - cost
        resources["money"] += cost
        print(f"Thank you for your payment. Here is your change: ${change:.2f}")
        return True


# Function to Check Resources and Return Coffee or Error
def check_resources(coffee_type):
    has_resources = True
    if resources["water"] < MENU[coffee_type]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        has_resources = False
    if resources["coffee"] < MENU[coffee_type]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        has_resources = False
    if (
        "milk" in MENU[coffee_type]["ingredients"]
        and resources["milk"] < MENU[coffee_type]["ingredients"]["milk"]
    ):
        print("Sorry there is not enough milk.")
        has_resources = False
    return has_resources


def used_resources(coffee_type):
    resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
    if "milk" in MENU[coffee_type]["ingredients"]:
        resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]


def coffee_machine():
    coffee_type = take_input()
    cost = MENU[coffee_type]["cost"]

    report_resources()

    has_resources = check_resources(coffee_type)
    if has_resources:
        used_resources(coffee_type)

        money = insert_money()

        has_paid = transaction(cost, money)
        if has_paid:
            print(f"Here is your {coffee_type} ☕.")
        report_resources()


print(LOGO)
while True:
    coffee_machine()



