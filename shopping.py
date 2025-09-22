#Available items in the store
store_items = {
    "apple": 50,
    "banana": 20,
    "milk": 30,
    "bread": 40
}

# Empty shopping cart
cart = {}

def show_items():
    print("\nAvailable Items:")
    for item, price in store_items.items():
        print(f"{item.capitalize()} - Rs {price}")
    print()

def add_to_cart():
    item = input("Enter the item you want to buy: ").lower()
    if item in store_items:
        quantity = int(input(f"Enter quantity of {item}: "))
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity
        print(f"{quantity} {item}(s) added to cart.")
    else:
        print("Item not available in the store!")

def view_cart():
    if not cart:
        print("\nYour cart is empty!\n")
        return
    print("\nItems in your cart:")
    total = 0
    for item, qty in cart.items():
        price = store_items[item] * qty
        print(f"{item.capitalize()} x {qty} = Rs {price}")
        total += price
    print(f"Total Amount = Rs {total}\n")

def checkout():
    view_cart()
    print("Thank you for shopping with us!")
    exit()

# Main menu
while True:
    print("===== Shopping Cart Menu =====")
    print("1. Show Store Items")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Checkout & Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        show_items()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        view_cart()
    elif choice == "4":
        checkout()
    else:
        print("Invalid choice! Please try again.")
    def checkout():
     view_cart()
    print("Thank you for shopping with us!")
    exit()

# Main menu
while True:
    print("===== Shopping Cart Menu =====")
    print("1. Show Store Items")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Checkout & Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        show_items()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        view_cart()
    elif choice == "4":
        checkout()
    else:
        print("Invalid choice! Please try again.")