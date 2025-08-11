temp = 0

for num in range(0, 11):
    temp = num * 4
    print(temp)
    if (temp == 12):
        print("the value is 12")
    continue  # maybe jump 1 (I need to return about this...)
    if (temp > 10):
        print("the value is more than 20")
    break  # if I understand right it's broke the loop with break
    print(f"temp is {temp}   ")

print("Test end")
