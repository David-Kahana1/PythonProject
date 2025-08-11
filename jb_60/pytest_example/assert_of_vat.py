prices = [20]
for price in prices:
    price_and_vat = price*1.18

assert price_and_vat<24, "The price is not valid"

print("Test End")
