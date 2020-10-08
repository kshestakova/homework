"""
Создайте словарь, в котором ключи - разные числа, значения - строки из файла 
(файл подготовьте вручную). Поменяйте значения в словаре: 
если строка начинается на гласную, переверните её (начало станет концом). 
Если строка начинается на буквы T, Р или K, удалите такую пару из словаря. 

"""

def print_dict(d):
    for k, v in d.items():
        print("{} : {}".format(k, v))
    print("___________________________________")

d = {}
with open("data_2_4.txt", "r") as data:
    lines = data.readlines()
    for i in range(len(lines)):
        d[i] = lines[i]
        
print_dict(d)

vowels = "eEuUiIoOaAyYуУеЕыЫаАоОэЭяЯиИюЮ"
symbols = "TPKtpkТРКтрк"

for key, value in d.items():
    if value[0] in vowels:
        d[key] = d[key][::-1]

print_dict(d)

a = []
for key in d.keys():
    if d[key][0] in symbols:
        a.append(key)
        
for i in a:
    del d[i]

print_dict(d)