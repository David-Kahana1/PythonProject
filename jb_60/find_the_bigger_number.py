#    home_work_1
#    We have 2 prices
#    26$ and 30$
#    Find the bigger number

num1 = '26$'
num2 = '30$'

index_1 = num1.index("$")
num1_new = num1[0:index_1]

index_2 = num2.index("$")
num2_new = num2[0:index_2]

num1_new = int(num1_new)
num2_new = int(num2_new)

if (num1_new > num2_new):
    print("number 1 price is bigger")
else:
    if (num1_new == num2_new):
        print("number 1 and number 2 is equals")
    else:
        print("number 2 price is bigger")

print("test end")
