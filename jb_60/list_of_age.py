


list_of_age = [-1, 0, 18, 19, 60, 61, 120, 121]

for age in list_of_age:

    if (0 <= age <= 18):
        print(f"{age} is child")
    elif (19 <= age <= 60):
        print(f"{age} is adult")
    elif (61 <= age <= 120):
        print(f"{age} is senior")
    else:
        print(f"{age} is error")

print("Test End")
