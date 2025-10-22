from main import MENU, resources

#I am gonna create main handling logic here
decision = ""
money=0.0
amount=0.0

def main_logic():
    global decision
    decision= input("What would you like? (espresso/latte/cappuccino): ")
    if  (decision=="espresso"):
        resource_check()
    elif (decision=="latte"):
        resource_check()
    elif (decision == "cappuccino"):
        resource_check()
    elif (decision == "report"):
        report_generation()
    elif (decision == "off"):
        print("You provided secret code for turning coffee machine off so now machine is turning off.")
        quit()
    else:
        print("Sorry Wrong input")

def report_generation():
    global money
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print (f"Money: ${money}")
    main_logic()

def resource_check():
    global decision
    if (decision=="espresso"):
        if (resources["water"] < MENU["espresso"]["ingredients"]["water"]):
            print("Sorry there is not enough water.")
            main_logic()
        elif (resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]):
            print("Sorry there is not enough coffee powder.")
            main_logic()
        else:
            process_coin()
    if (decision == "latte"):
        if (resources["water"] < MENU["latte"]["ingredients"]["water"]):
            print("Sorry there is not enough water.")
            main_logic()
        elif (resources["milk"] < MENU["latte"]["ingredients"]["milk"]):
            print("Sorry there is not enough milk.")
            main_logic()
        elif (resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]):
            print("Sorry there is not enough coffee powder.")
            main_logic()
        else:
            process_coin()
    if (decision == "cappuccino"):
        if (resources["water"] < MENU["cappuccino"]["ingredients"]["water"]):
            print("Sorry there is not enough water.")
            main_logic()
        elif (resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]):
            print("Sorry there is not enough milk.")
            main_logic()
        elif (resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]):
            print("Sorry there is not enough coffee powder.")
            main_logic()
        else:
            process_coin()

#Here the process of coin is gonna take place
def process_coin():
    global amount
    print("Please insert coins")
    quarters=int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    amount=(quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)
    transaction()

# Here transaction is being processed
def transaction():
    global decision, amount, money
    if (decision=="espresso"):
        if(amount<MENU["espresso"]["cost"]):
            print("Sorry that's not enough money. Money refunded.")
            main_logic()
        elif(amount==MENU["espresso"]["cost"]):
            money = money + amount
            make_coffee()
        else:
            remaining=round(amount - MENU["espresso"]["cost"], 2)
            money = money + MENU["espresso"]["cost"]
            print(f"Here is ${remaining} dollars in change.")
            make_coffee()
    elif (decision=="latte"):
        if(amount<MENU["latte"]["cost"]):
            print("Sorry that's not enough money. Money refunded.")
            main_logic()
        elif(amount==MENU["latte"]["cost"]):
            money = money + amount
            make_coffee()
        else:
            remaining=round(amount - MENU["latte"]["cost"], 2)
            money = money + MENU["latte"]["cost"]
            print(f"Here is ${remaining} dollars in change.")
            make_coffee()
    elif (decision=="cappuccino"):
        if(amount<MENU["cappuccino"]["cost"]):
            print("Sorry that's not enough money. Money refunded.")
            main_logic()
        elif(amount==MENU["cappuccino"]["cost"]):
            money = money + amount
            make_coffee()
        else:
            remaining=round(amount - MENU["cappuccino"]["cost"], 2)
            money = money + MENU["cappuccino"]["cost"]
            print(f"Here is ${remaining} dollars in change.")
            make_coffee()
    else:
        print("Sorry Wrong input.")

def make_coffee():
    global decision, money
    if (decision=="espresso"):
        resources["water"]=resources["water"]-MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
        print("Here is your espresso 🍵 Enjoy!")
        main_logic()
    elif (decision=="latte"):
        resources["water"]=resources["water"]-MENU["latte"]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
        print("Here is your latte 🍵 Enjoy!")
        main_logic()
    elif (decision=="cappuccino"):
        resources["water"]=resources["water"]-MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
        print("Here is your cappuccino 🍵 Enjoy!")
        main_logic()
    else:
        print("Sorry Wrong input.")


def main():
    main_logic()

main()
