cart = ["apple", "banana", "milk", "apple", "eggs"]
apple_count = cart.count("apple")
print(f"Number of apples: {apple_count}")
print(f"Position of Milk: {cart.index("milk")}")
cart.remove("apple")
print(f"removed item used pop: {cart.pop()}")
print("is banana in the cart?", "banana" in cart)
print(f"Final cart: {cart}")
