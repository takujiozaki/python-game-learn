list = [
    {"date":'2020-07-06', 'action': '指定来所日'},
    {"date":'2020-06-15', 'action': '就職活動日'},
    {"date":'2020-08-15', 'action': '盆休み'},
]

# print(list)

list2 = sorted(list, key=lambda x: x['date'])

print(list2)