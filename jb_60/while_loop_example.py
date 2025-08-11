

is_pass= False
counter = 0
while not (is_pass):
    print("the value of is pass is True")
    print(counter)
    counter+=1
    if (counter==5):
        is_pass = True
        continue
    if (counter>10):
        break
