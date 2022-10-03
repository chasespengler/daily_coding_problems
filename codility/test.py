z = {
    'id': 763,
    'customer_id': 14
}

print(z['id'])

import datetime

day = datetime.date(2021, 4, 4)
print(day.day)

my = "2022-04"
print(int(my[-2:]))
if day.year < int(my[0:4]):
    print("FUCK")
print(int(my[0:4]))
print(day.day * 2)
