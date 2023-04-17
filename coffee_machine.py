from shop_data import MENU


resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100
}
## todo1 is resouce sufficient funtion
def is_sufficient_resources(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
             return False
    return True

##todo2 process coin function to calculate total amount of money user insert
def process_coin():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


##todo3 is transaction successful if user insert sufficient money
def is_transaction_successful(received_money,cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if received_money < cost:
        print("Sorry, that is not enouth money, money refunded")
        return False
    change = received_money - cost
    change = round(change,2)
    print(f"{change} amount is change")
    return True

##todo4 make coffee by checking resources with item in order ingredients if and update resources list after making coffee

def make_coffee(drink_name,order_item):
    """Deduct the required ingredients from the resources."""
    for item in order_item:
        resources[item] = resources[item] - order_item[item]
    print(f"here is your {drink_name} ☕. enjoy")
    

##todo5 finally make one coffee machine funtion call all other funtion to excute process



def coffe_order():
    is_on = True
    while is_on:
        choice = input("what would you like espresso/latte/cappuccino : ").lower()
        if choice == "off":
            is_on = False
        elif choice == "report":
            print("Available resources: ")
            print(f"water : {resources['water']}ml")
            print(f"milk : {resources['milk']}ml")
            print(f"coffee : {resources['coffee']}")
        else:
            if is_sufficient_resources(MENU[choice]['ingredients']):
                money_received = process_coin()
                if is_transaction_successful(money_received,MENU[choice]['cost']):
                    make_coffee(choice, MENU[choice]['ingredients'])



coffe_order()