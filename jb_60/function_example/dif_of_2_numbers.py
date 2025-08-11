# 1. Create a function that accepts 2 numbers and prints all the numbers between them
#    The function must be run on all states


from jb_60.function_example.utils import utils

utils_instance= utils()

num_1= 1
num_2= 10
num_3= 27

utils_instance.print_between_numbers(num_1,num_2)
print(f"#############")
utils_instance.print_between_numbers(num_3,num_2)
print(f"#############")

print("Test End")