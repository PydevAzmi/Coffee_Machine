from Data import coffee
complete = "yes"
while complete != "no":
    coffee_required = input("What would you like? (Espresso/Latte/Cappuccino)").lower()
    if coffee_required == "off":
        complete = "off"
        break
    elif coffee_required == "report":
        print(f"Water :  {coffee[0]['report']['Water']}ml")
        print(f"Milk :  {coffee[0]['report']['Milk']}ml")
        print(f"Coffee :  {coffee[0]['report']['Coffee']}mg")
        print(f"Money :  {coffee[0]['report']['Money']}$")
    elif coffee_required == "espresso" or coffee_required == "latte" or coffee_required == "cappuccino":
        print("Please insert coins .")
        quarters = int(input("how many quarters : "))
        dimes = int(input("how many dimes : "))
        nickles = int(input("how many nickles : "))
        pennies = int(input("how many pennies : "))
        money_entered = quarters * 0.25 + dimes * 0.10 + pennies * 0.01 + nickles * 0.05
        print(f"the money you Entered =  {money_entered}")


        def check_resources(cof_name, money):
            # global coffee
            if coffee[0]["report"]["Water"] >= coffee[0][cof_name]["Water"]:
                if coffee[0]["report"]["Milk"] >= coffee[0][cof_name]["Milk"]:
                    if coffee[0]["report"]["Coffee"] >= coffee[0][cof_name]["Coffee"]:
                        if money >= coffee[0][cof_name]["Money"]:
                            coffee[0]["report"]["Water"] -= coffee[0][cof_name]["Water"]
                            coffee[0]["report"]["Milk"] -= coffee[0][cof_name]["Milk"]
                            coffee[0]["report"]["Coffee"] -= coffee[0][cof_name]["Coffee"]
                            coffee[0]["report"]["Money"] += money
                            return "Your cup is ready \nThank You for using us."
                        else:
                            return "Sorry there is not enough Money, The Money is refunded. "
                    else:
                        return "Sorry there is not enough coffee."
                else:
                    return "Sorry there is not enough milk."
            else:
                return "Sorry there is not enough water."


        message = check_resources(coffee_required, money_entered)
        print(message)
    else:
        print("please enter supported kind of coffee ")
    complete = input("do you want try again . (Yes or No)").lower()


