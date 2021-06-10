"""Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
name - строка полученная от пользователя,
health = 100,
damage = 50.
### Поэкспериментируйте с значениями урона и жизней по желанию.
# ### Теперь надо создать функцию attack(person1, person2).
# Примечание: имена аргументов можете указать свои.
# ### Функция в качестве аргумента будет принимать атакующего и атакуемого.
# ### В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения."""
import random

def block():
    print("-" * 50)

def attack(person_1, person_2):
    person_1 = player["name"]
    person_2 = enemy['name']
    print('Атакует {} и наносит {} урона игроку {}'.format(person_1, player['damage'], person_2))
    enemy ['health'] = enemy['health'] - player ['damage']
    print(('У {} осталось {} здоровья').format(person_2, enemy['health']))
    block()
    print('Атакует {} и наносит {} урона игроку {}'.format(person_2, enemy['damage'], person_1))
    player['health'] = player['health'] - enemy['damage']
    print(('У {} осталось {} здоровья').format(person_1, player['health']))
    block()

player = {
    'name': "",
    'health': 100,
    'damage': random.randint(50, 100)
}
player['name'] = input("Введите имя Вашего персонажа: \n")

enemy = {
    'name': '',
    'health': 200,
    'damage': random.randint(20, 50)
}
enemy['name'] = input("Введите имя вашего противника: \n")

block()

for key, val in player.items():
    print(key + " - " + str(val))

block()

for key, val in enemy.items():
    print(key + " - " + str(val))

block()

while True:
    attack(player, enemy)
    if player['health'] <= 0:
        print("Победил " + enemy['name'])
        break
    elif enemy['health'] <= 0:
        print("Победил " + player['name'])
        break
