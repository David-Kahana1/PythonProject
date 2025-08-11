# home_work_2
# We have full name according
#           "John_Due"
#  Find what is longer first name or last name.

full_name = "John_Due"
index = full_name.index("_")

first_name = full_name[0:index]
length = len(full_name)
last_name = full_name[index + 1:length]
length_1 = len(first_name)
length_2 = len(last_name)

if (length_1 > length_2):
    print("first name is longer")
else:
    if (length_1 == length_2):
        print("first name and last name is equals")
    else:
        print("last name is longer")

print("test end")
