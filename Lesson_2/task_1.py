""": Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
    Примечание. Списки создайте вручную, например так:
my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
"""

my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
print(my_list_1)
print(my_list_2)
for i in my_list_1:
    if i in my_list_2:
        my_list_1.remove(i)
print()
print(my_list_1)