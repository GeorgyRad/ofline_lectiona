"""Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
Следовательно, у вас должно быть 2 функции:
Наносит урон. Это улучшенная версия функции из задачи 3.
Вычисляет урон по отношению к броне.

Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа. """

import random

def block():
    print("-" * 50)

def attack(person_1, person_2):
    person_1 = player["name"]
    person_2 = enemy['name']
    damage = armor(person_1, person_2)
    print('Атакует {} и наносит {} урона игроку {}'.format(person_1, player['damage'], person_2))
    enemy   ['health'] = enemy['health'] - player ['damage']
    print(('У {} осталось {} здоровья').format(person_2, enemy['health']))
    block()
    print('Атакует {} и наносит {} урона игроку {}'.format(person_2, enemy['damage'], person_1))
    player['health'] = player['health'] - enemy['damage']
    print(('У {} осталось {} здоровья').format(person_1, player['health']))
    block()

def armor(person_1, person_2):
    person_1 = player['name']
    person_2 = enemy['name']
    player['damage'] = player['damage']/enemy['armor']
    enemy['damage'] = enemy['damage']/player['damage']

player = {
    'name': "",
    'health': 100,
    'damage': 84,
    'armor': 1.2
}
player['name'] = input("Введите имя Вашего персонажа: \n")

enemy = {
    'name': '',
    'health': 200,
    'damage': 32,
    'armor': 1.2
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
