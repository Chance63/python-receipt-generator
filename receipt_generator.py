item_name = input("Please enter item name: ")

unit_price = float(input("Please enter the unit price: "))

quantity_purchased = int(input("Please enter quantity purchased: "))

discount1 = float(input("Please enter employee/student discount percent: "))

tax = float(input("Please enter sales tax percent: "))

quantity = quantity_purchased * unit_price

subtotal = quantity

discount2 = subtotal * (discount1 / 100)

Taxable_amount = subtotal - discount2

tax2 = Taxable_amount * (tax / 100)

total_due = Taxable_amount + tax2

print("_____Receipt_____")

print(f"item: {item_name}")

print(f"Qty x Unit: ${quantity_purchased} * {unit_price}")

print("_________________")

print(f"Subtotal: ${subtotal}")

print(f"Discount ({discount1}%): ${discount2}")

print(f"Taxable Amount: ${Taxable_amount}")

print(f"Tax ({tax}%): ${tax2}")

print("_________________")

print(f"Total Due: ${total_due}")

print("_________________")

print("Thank you For Your Purchase!")
