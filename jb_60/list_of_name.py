# 3. Read an array of names and print the longest name

name_list = ["Boaz", "Steph", "Lebron", "Giannis", "Donald", "Tom"]
longest_name = 0

for name in name_list:
    len_name = len(name)
    if (len_name > longest_name):
        longest_name = len_name
        the_bigger_name = name

print(f"the longest name is {the_bigger_name},({longest_name}).")

print("Test End")

# we have a problem if 2 names in the list is equals.