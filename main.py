from functools import total_ordering
from itertools import count
from random import choice
from tkinter.messagebox import RETRY
from colorama import Fore
MENU= {
    "espresso": {
        "ingredients":{
            "water": 50,
            "coffee": 18,
        },
        "cost":1.5
    },
    "latte": {
        "ingredients": {
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost": 2.5,
    },
    "cappucino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def isResourceSufficient(order_ingredients):
    """Returns the total calculated from coins instered."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry is there not enough {item}")
            return False
    return True

def processCoins():
    """Returns the total calculated from coins insterted."""
    print("PLease insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def isTransactionSuccesfull(moneyReceived, drinkCost):
    if moneyReceived >= drinkCost:
        change= round(moneyReceived - drinkCost, 2)
        print(f"Here is {change} in change!")
        global profit
        profit += drinkCost
        return True
    else:
        print("Sorry that's not enough money. MOney refunded.")
        return False


def makeCoffee(drinkName, orderIngredients):
    for item in orderIngredients:
        resources[item] -= orderIngredients[item]
    print(f"Here is your {drinkName} ☕☕☕!")


profit= 0
isOn= True
while isOn:
    choice=input("What would you like? (espresso/latte/cappucino): ")
    if choice == "off":
        isOn = False
    elif choice == "report":
        print(f"Water: {resources["water"]}ml ")
        print(f"Milk: {resources["milk"]}ml ")
        print(f"Coffee : {resources["coffee"]}g")
        print(f"Money : ${profit}")
    else:
        drink=MENU[choice]
        if isResourceSufficient(drink["ingredients"]):
            payment= processCoins()
            if isTransactionSuccesfull(payment,drink["cost"]):
                makeCoffee(choice, drink["ingredients"])
