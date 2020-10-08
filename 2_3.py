"""
Создайте словарь, в котором ключи - разные числа, значения - рандомные числа (любые). 
Напишите генератор списка из элементов-произведений “ключ” * “значение”. 

"""

from random import randint

d = {}

for i in range(100):
    d[i] = randint(0, 1000)
    
l = [key * value for key, value in d.items()]

print(d)
print(l)