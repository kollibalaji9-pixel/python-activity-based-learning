print("PRODUCT CATALOGUE AUDIT")

products = []
n = int(input("Enter number of products: "))

for i in range(n):
    print("\nProduct", i + 1)
    product_id = input("Enter product ID: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter stock quantity: "))
    products.append((product_id, price, stock))

print("\nPRODUCT AUDIT REPORT")
total_inventory_value = 0

for product in products:
    product_id, price, stock = product  # Tuple unpacking
    print("\nProduct ID:", product_id)

    if price < 0 or stock < 0:
        print("Status: Invalid Record")
    else:
        value = price * stock
        total_inventory_value += value
        print("Price: Rs.", price)
        print("Stock:", stock)
        print("Inventory Value: Rs.", value)

        if stock < 10:
            print("Replenishment Required")
        else:
            print("Stock Status: Sufficient")

print("\nTotal Inventory Value: Rs.", total_inventory_value)
