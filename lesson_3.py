var_year = 1998

if var_year > 2000:
    print("Generation Z")
elif var_year % 2 == 0:
    print("Born in even year")
else:
    print("Born in uneven year")


def print_first_name(first_name: str):
    """Prints the first name"""
    print("My name is " + first_name)


def print_full_name(first_name, last_name):
    """Prints the first name and the last name"""
    print(first_name + " " + last_name)


print_first_name("Emily")
