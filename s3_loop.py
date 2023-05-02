years = range(1980, 2021, 1)


def is_leap_year(year):
    if year % 4 > 0:
        return False
    elif year % 100 > 0:
        return True
    elif year % 400 > 0:
        return False
    else:
        return True


for year in years:
    if is_leap_year(year):
        print(year)
