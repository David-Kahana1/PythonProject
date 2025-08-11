numbers = [3,5,6,7,12,13,67,78]
cities = ["London", "Athens", "New-York", 'Jerusalem', 'Lod']

for city in cities:
    city_len = len(city)
    print(f"{city},{city_len}")
    if (city.count("-") > 0):
        print(f"- found at {city}")
        break

print("Test End")

#l= len(numbers)
value = numbers [2]
index_of_5 = numbers.index(5)
numbers.append(56)
numbers.insert(2,77)
counter = numbers.count(6)

for number in numbers:
    print (number)
    if (number < 10):
        print (f"found number less than 10")
        number+=10

    if (number%2 == 0):
        print(f"{number} dived by 2")

print("Test End")


prices = [12,45,67,32,34]

for price in prices:
    price_and_VAT= price*1.18
    price_and_VAT=round(price_and_VAT)
    print(f"{price_and_VAT} is the new price")