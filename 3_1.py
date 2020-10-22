""" Создайте класс, который будет описывать ваш фильм. Давайте назовём его Movie. 
У него должны быть следующие атрибуты: name, duration, releaseDate и rating. 

Для класса Movie определите метод с именем show_info(), 
который выводит на экран параметры вашего фильма, значение атрибутов объекта 
(name, duration и rating). 
"""
class Movie:
    def __init__(self, name = "Noname", duration = 0, releaseDate = 1970, rating = 0.0):
        self.name = name
        self.duration = duration
        self.releaseDate = releaseDate
        self.rating = rating
        
    def show_info(self):
        print("Film:", self.name)
        print("Duration: {h}:{m}".format(h = self.duration//60, m = self.duration%60))
        print("Release date:", self.releaseDate)
        print("Rating:", self.rating, "\n")

"""
Создайте 10 объектов класса Movie, это должны быть ваши самые любимые фильмы. 
Информацию о них можно взять на imdb или в каком-то другом месте. 
"""

movies = []
with open ("films.txt", "r") as films:
    for s in films:
        s = s.split(", ")
        movies.append(Movie(s[0], int(s[1]), int(s[2]), float(s[3])))

"""
Создайте класс Сritic, это и будете вы. 
Дадим этому классу самые базовые атрибуты - name и age. 
Кроме того, будем хранить в классе список из ваших фильмов.
Создайте функции для класса Сritic:
Вывод информации о самом длинном фильме
Вывод информации о фильме с самым высоким рейтингом
Вывод суммарной длительности всех фильмов в списке
"""

class Critic:
    def __init__(self, name = "Me", age = 15, movies = []):
        self.name = name
        self.age = age
        self.movies = movies
    
    def longest(self):
        longest = self.movies[0]
        for m in self.movies[1:]:
            if m.duration > longest.duration:
                longest = m
        
        print("The longest movie:")
        longest.show_info()
        
    def highest(self):
        highest = self.movies[0]
        for m in self.movies[1:]:
            if m.rating > highest.rating:
                highest = m
        
        print("Movie with the highest rating:")
        highest.show_info()

    def totalTime(self):
        s = 0
        for m in self.movies:
            s += m.duration
        
        print("Total time: {h}:{m}".format(h = s//60, m = s%60))

me = Critic("Kseniia", 34, movies)
me.longest()
me.highest()
me.totalTime()

