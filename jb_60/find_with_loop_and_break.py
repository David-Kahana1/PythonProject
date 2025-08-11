#    home_work_4
#    find by loop when the square value is more than 25.


for num in range(1, 11):
    num_1 = (num)
    num = (num * num)
    if (num > 25):
        print(f"in {num_1} the value is more than 25")
        break

print("test end")
