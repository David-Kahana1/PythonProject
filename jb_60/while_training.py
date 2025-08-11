is_pass = True
counter = 0

while (is_pass):
    print(counter)
    counter += 1
    if (counter % 7 == 0):
        is_pass = False

    if (counter==20):
        print("we got max value loop stoped")
        break

print("Test End")

#with for lop
for i in range (1,20):
    print(f"the value of i is {i}")
    if (i%7==0):
        break

print("Test End")