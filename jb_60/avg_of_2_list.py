list_numbers_1= [5,3,4,677,89,9,4,2,81,23]
list_numbers_2= [2,3,4,56,2,77,88,3,210,450]


len_1 = len(list_numbers_1)
sum_1 = sum(list_numbers_1)
avg_1 = sum_1/len_1


len_2 = len(list_numbers_2)
sum_2 = sum(list_numbers_2)
avg_2 = sum_2/len_2

if (avg_1 > avg_2):
    print(f"the average of the first list is bigger (avg:{avg_1})")
elif (avg_1 == avg_2):
    print(f"the average of all the list is equals (avg:{avg_1})")
else:
    print(f"the average of the second list is bigger (avg:{avg_2})")

print("Test End")