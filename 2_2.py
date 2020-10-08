"""
Напишите генератор автомобильных номеров Украины: 
две буквы, четыре цифры, две буквы. 
Варианты первых двух букв здесь 
https://www.ukrstrahovanie.com.ua/wp-content/uploads/2018/08/avo-nomera.jpg, 
последние две могут быть из строки ETIOPAHKXCB.

"""
first_letters = ["AA", "AB", "AC", "AE", "AH", "AI", "AK", "AM", "AO", "AP", "AT", "AX", 
                 "BA", "BB", "BC", "BE", "BH", "BI", "BK", "BM", "BO", "BT", "BX", 
                 "CA", "CB", "CE", "CH"]

digits = [i for i in range(10)]

last_letters = [i for i in "ETIOPAHKXCB"]

gen = (e + str(a) + str(b) + str(c) + str(d) + i + j
    for e in first_letters
    for a in digits for b in digits for c in digits for d in digits
    for i in last_letters for j in last_letters)

with open("result_2_2.txt", "w") as result:
    for t in gen:
        result.write("{}\n".format(t))