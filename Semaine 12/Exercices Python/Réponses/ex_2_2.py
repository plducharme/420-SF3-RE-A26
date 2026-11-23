# 2.2 Le dé du destin
import random

lancers = []
for i in range(10):
    lancers.append(random.randint(1, 6))
print('Lancers :', lancers)
moyenne = sum(lancers) / len(lancers)
print(f'Max : {max(lancers)}   Min : {min(lancers)}   Moyenne : {moyenne}   Nombre de 6 : {lancers.count(6)}')
