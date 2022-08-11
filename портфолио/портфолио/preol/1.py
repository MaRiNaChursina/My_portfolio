
name = input("Имя")
size = input("Размер")
n = int (input("Количество чел в команде"))
players = {}
name = input("Введите имя человека")
players[name] = size
for i in range(n):
    if name in players:
        print(players[name])
    else:
        print("Такого человека в команде нет")