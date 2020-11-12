"""
Создайте базовый класс для абстрактной фигуры и классы-наследники для различных 
геометрических фигур. Пусть в базовом классе будут функции вывода площади и периметра 
и соответствующие переменные, а также вывод полной информации  о фигуре (имя фигуры, площадь, 
периметр). 
Для каждого из классов-наследников определите функции задания параметров (можно в конструкторе), 
изменения параметров, расчета площади, расчета периметра и вывода на экран (через pygame). 
В цикле сгенерируйте 10 любых фигур (лучше разных), выведите их на экран и в консоли 
для каждой рассчитайте площадь и периметр. 
""" 

import pygame

pygame.init()
surface = pygame.display.set_mode((1200, 1000))
pygame.display.set_caption("Figures")

BLUE = (0, 204, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

PI = 3.14

class Figure:
    # x, y - координаты, к которым привязываемся при рисовании (левый верхний угол или центр)
    def __init__(self, x = 0, y = 0):
        self.perimeter = 0
        self.space = 0
        self.color = WHITE
        self.x = x
        self.y = y
    def calcPerimeter(self): 
        pass
    def calcSpace(self): 
        pass
    def figInfo(self): 
        self.calcPerimeter()
        self.calcSpace()
        print('Периметр = %s, площадь = %s' %(self.perimeter, self.space))
    def draw(self, surface):
        pygame.display.update()
        
class Square(Figure):
    # x, y - координаты левого верхнего угла, w - длина стороны
    def __init__(self, x, y, w):
        Figure.__init__(self, x, y)
        self.w = w
        self.color = RED
    def calcPerimeter(self):
        self.perimeter = self.w * 4
    def calcSpace(self):
        self.space = self.w * self.w
    def figInfo(self):
        print('Квадрат')
        super().figInfo()
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.w, self.w), 5)
        super().draw(surface)
        
class Rectangle(Square):
    # x, y - координаты левого верхнего угла, w, h - ширина и высота
    def __init__(self, x, y, w, h):
        Square.__init__(self, x, y, w)
        self.h = h
        self.color = BLUE
    def calcPerimeter(self):
        self.perimeter = self.w * 2 + self.h * 2
    def calcSpace(self):
        self.space = self.w * self.h
    def figInfo(self):
        print('Прямоугольник')
        Figure.figInfo(self)
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.w, self.h), 5)
        Figure.draw(self, surface)

class Circle(Figure):
    # x, y - координаты центра, r - радиус
    def __init__(self, x, y, r):
        Figure.__init__(self, x, y)
        self.r = r
        self.color = YELLOW
    def calcPerimeter(self):
        self.perimeter = self.r * 2 * PI
    def calcSpace(self):
        self.space = self.r * self.r * PI
    def figInfo(self):
        print('Круг')
        super().figInfo()
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.r, 5)
        super().draw(surface)
        
# равнобедренная трапеция        
class Trapezoid(Figure):
    # x, y - координаты левого верхнего угла, a, b - длины оснований, c - длина стороны
    def __init__(self, x, y, a, b, c):
        Figure.__init__(self, x, y)
        # чтобы a >= b
        if a > b:
            self.a = a
            self.b = b
        else:
            self.a = b
            self.b = a
        self.c = c
        self.color = GREEN
        # вычислим высоту, пригодится для расчетов и рисования
        self.h = (self.c**2 - (self.a-self.b)**2 / 4)**0.5
    def calcPerimeter(self):
        self.perimeter = self.a + self.b + self.c * 2 
    def calcSpace(self):
        self.space = (self.a + self.b) / 2 * self.h
    def figInfo(self):
        print('Трапеция')
        super().figInfo()
    def draw(self, surface):
        d = (self.a - self.b)/2
        k = [self.x + d, self.y]
        l = [self.x + d + self.b, self.y]
        m = [self.x + self.a, self.y + self.h]
        n = [self.x, self.y + self.h]
        pygame.draw.lines(surface, self.color, True, [k, l, m, n], 5)
        super().draw(surface)
        
class Ellipse(Figure):
    # x, y - левый верхний угол, a, b - длины осей
    def __init__(self, x, y, a, b):
        Figure.__init__(self, x, y)
        self.a = a
        self.b = b
    def calcPerimeter(self):
        self.perimeter = 2 * PI * ((self.a ** 2 + self.b ** 2) / 8) ** 0.5
    def calcSpace(self):
        self.space = PI * self.a * self.b / 4
    def figInfo(self):
        print('Эллипс')
        super().figInfo()
    def draw(self, surface):
        pygame.draw.ellipse(surface, self.color, (self.x, self.y, self.a, self.b), 5)
        super().draw(surface)
        
if __name__ == '__main__':
    fig = Figure()
    fig1 = Rectangle(5, 5, 100, 150)
    fig2 = Square(50, 50, 100)
    fig3 = Circle(100, 100, 30)
    fig4 = Trapezoid(150, 150, 40, 100, 50)
    fig5 = Ellipse(50, 100, 300, 100)
    array = [fig1, fig2, fig3, fig4, fig5]
    for f in array:
        # вот здесь я не знаю, какого конкретно класса у меня объект
        # но вызываю для него две функции, которые в нем точно есть
        # и их поведение зависит от конкретного класса
        f.figInfo()
        f.draw(surface)
        
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()