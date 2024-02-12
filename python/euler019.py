
import calendar


DAYS_PER_MONTH = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


def weekday(day, month, year):
    year_difference = year - 1901
    year_days = (365 * year_difference) + (year_difference // 4)
    month_days = sum([DAYS_PER_MONTH[i] for i in range(1, month)])
    if (year % 4 == 0) and (month > 2):
        month_days += 1
    return 1 + ((1 + (year_days + month_days + day)) % 7)


counter = 0
for year in range(1901, 2001):
    print(year, weekday(1, 1, year), ((calendar.weekday(year, 1, 1) + 1) % 7) + 1)
    for month in range(1, 13):
        if weekday(1, month, year) == 1:
            counter += 1

# The answer is 171
print(counter)
