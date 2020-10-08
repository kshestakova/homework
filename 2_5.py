"""
Создайте словарь, в котором значением будет достаточно длинная строка, 
а ключом - её хэш. В качестве хэш-функции, которая вычисляет хэш по строке, 
возьмите sha1 из библиотеки hashlib (import hashlib, a = hashlib.sha1(“some_string”). 
Запишите словарь в файл, отсортировав хэши в алфавитном порядке. 

"""

import hashlib

dict = {}
 
with open("data_2_5.txt", "r") as data:
    for line in data.readlines():
        line = line.encode("utf-8")
        hash_object = hashlib.sha1(line).hexdigest()
        dict[hash_object] = line.decode()
        
a = sorted(dict.keys())

with open("result_2_5.txt", "w") as result:
    for i in a:
        result.write("{} : {}".format(i, dict[i]))
 
