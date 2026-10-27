print("RETAIL BILLING SYSTEM")

products = []
total = 0
n = int(input("Enter number of products: "))

for i in range(n):
    print("\nProduct", i + 1)
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    if price < 0 or quantity < 0:
        print("Invalid product details; product skipped.")
        continue

    amount = price * quantity
    products.append((name, price, quantity, amount))
    total += amount

if total >= 5000:
    discount_rate = 0.15
elif total >= 2000:
    discount_rate = 0.10
elif total >= 1000:
    discount_rate = 0.05
else:
    discount_rate = 0

discount = total * discount_rate
final_amount = total - discount

print("\nRETAIL INVOICE")
for name, price, quantity, amount in products:
    print("Product:", name, "| Price:", price,
          "| Quantity:", quantity, "| Amount:", amount)

print("Total Amount: Rs.", total)
print("Discount: Rs.", discount)
print("Final Amount: Rs.", final_amount)
