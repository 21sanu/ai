import random

orders = {
    "101": {"name": "Alice", "product": "Laptop", "quantity": 1, "status": "Processing"},
    "102": {"name": "Bob", "product": "Headphones", "quantity": 2, "status": "Shipped"}
}

facts = [
    "Tip: Compare prices before buying!",
    "Free shipping increases buying chances!",
    "Reviews can give discounts!"
]

def chatbot():
    print("Welcome to QuickCart Bot")

    while True:
        print("\n1.View Order\n2.Cancel Order\n3.Update Address\n4.Fun Fact\n5.Exit")
        ch = input("Enter choice: ")

        if ch == "1":
            oid = input("Enter Order ID: ")
            if oid in orders:
                o = orders[oid]
                print("Name:", o["name"])
                print("Product:", o["product"])
                print("Quantity:", o["quantity"])
                print("Status:", o["status"])
            else:
                print("Order not found")

        elif ch == "2":
            oid = input("Enter Order ID: ")
            if oid in orders:
                if orders[oid]["status"] == "Processing":
                    orders[oid]["status"] = "Cancelled"
                    print("Order cancelled")
                else:
                    print("Cannot cancel, already", orders[oid]["status"])
            else:
                print("Order not found")

        elif ch == "3":
            oid = input("Enter Order ID: ")
            if oid in orders:
                addr = input("Enter new address: ")
                orders[oid]["address"] = addr
                print("Address updated")
            else:
                print("Order not found")

        elif ch == "4":
            print("Fun Fact:", random.choice(facts))

        elif ch == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice")

chatbot()