# This Function to shows all products with category, price, and stock
def display_products():
    print("\nWelcome to Beauty Glam Vending Machine Gorgeous!!")
    for category in products:
        print(f"\nCategory: {category}")
        for code in products[category]:
            item = products[category][code]
            print(f"{code} : {item['name']} - {item['price']} dh (Stock: {item['stock']})")
            
#function to allow the user to select a product
def select_product():
    while True:
        code = input("\nKindly enter a product code: ")

        for category in products:
            for item_code in products[category]:
                if code == str(item_code):
                    item = products[category][item_code]
                     # Check if item is available
                    if item["stock"] > 0:
                        return category, item_code
                    else:
                        print("Sorry, this item is out of stock T.T .")
                        break

        print("Invalid product code. Please try again.")
        

# Function to handle payment process
def payment(price):
    money = float(input(f"Enter money (Price: {price} dh): "))

    while money < price:
        money += float(input("Not enough money, add more: "))

    change = money - price
    print(f"Your change is {change} dh.")

# Main vending machine function with loops
def vending_machine():
    print("\nWelcome to Beauty Glam Vending Machine gorgeous!!")

    choice = input("Would you like to buy something? (Yes/No): ")

    if choice.lower() != "yes":
        print("Thank you! Have a nice day gorgeous!!")
        return

    while True:
        display_products()

        category, code = select_product()
        item = products[category][code]

        payment(item["price"])

        item["stock"] = item["stock"] - 1
        print(f"{item['name']} has been dispensed")

        again = input("\nDo you want to buy another item? (yes/no): ")
        if again.lower() != "yes":
            print("Thank you for shopping at Beauty Glam gorgeous!!")
            print("ALWAYS REMEMBER YOU ARE BEAUTIFUL! LOVE YOUU BYEE!")
            break

# Dictionary storing all products with their details
products = {
    "Blush": {
        1: {"name": "Rosey red", "price": 20, "stock": 5},
        2: {"name": "Cherry blossom", "price": 20, "stock": 5},
        3: {"name": "Peach girl", "price": 20, "stock": 5},
        4: {"name": "Desier", "price": 20, "stock": 5},
        5: {"name": "Love", "price": 20, "stock": 5},
        6: {"name": "Berry", "price": 20, "stock": 5}
    },    
    "Lipsick": {
        7: {"name": "Rose pink", "price": 15, "stock": 5},
        8: {"name": "Wine red", "price": 15, "stock": 5},
        9: {"name": "Pinky orange", "price": 15, "stock": 5},
        10: {"name": "Cola red", "price": 15, "stock": 5},
        11: {"name": "Classic reds", "price": 15, "stock": 5},
        12: {"name": "Espreso", "price": 15, "stock": 5}
    },    
    "Eyeshadow": {
        13: {"name": "Soft glam", "price": 25, "stock": 5},
        14: {"name": "Gruge", "price": 25, "stock": 5},
        15: {"name": "Rainbow pop", "price": 25, "stock": 5},
        16: {"name": "Dark night", "price": 25, "stock": 5},
        17: {"name": "Chocolate power", "price": 25, "stock": 5}
    },  
    "Eyeliner": {
        18: {"name": "Black", "price": 10, "stock": 5},
        19: {"name": "Brown", "price": 10, "stock": 5},
        20: {"name": "White", "price": 10, "stock": 5},
        21: {"name": "Gliter", "price": 10, "stock": 5},
        22: {"name": "Red", "price": 10, "stock": 5}
    },
    "Mascara": {
        23: {"name": "Volume", "price": 16, "stock": 5},
        24: {"name": "Length", "price": 16, "stock": 5},
        25: {"name": "Curl", "price": 16, "stock": 5},
        26: {"name": "Tubing", "price": 16, "stock": 5}
    },
    "Eye Lashes set": {
        27: {"name": "All round", "price": 20, "stock": 5},
        28: {"name": "Round", "price": 20, "stock": 5},
        29: {"name": "Half", "price": 20, "stock": 5},
        30: {"name": "Cat eye", "price": 20, "stock": 5},
        31: {"name": "Fox eye", "price": 20, "stock": 5}
    }
}

vending_machine()
