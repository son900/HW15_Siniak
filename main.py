# task 1
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Figure):
    def __init__(self, a, b):
        self.b = b
        self.a = a

    def area(self):
        return self.a * self.b

    def __str__(self):
        return f'Площадь прямоугольника равна: {self.area()}'


class Circle(Figure):
    def __init__(self, r):
        self.r = r
        self.p = 3.14

    def area(self):
        return self.p * self.r

    def __str__(self):
        return f'Площадь круга равна: {self.area()}'


class RightTriangle(Figure):
    def __init__(self, leg_a, leg_b):
        self.leg_a = leg_a
        self.leg_b = leg_b

    def area(self):
        return 1/2 * (self.leg_a * self.leg_b)

    def __str__(self):
        return f'Площадь прямоугольного треугольника равна: {self.area()}'


class Trapezoid(Figure):
    def __init__(self, base_a, base_b, height):
        self.base_a = base_a
        self.base_b = base_b
        self.height = height

    def area(self):
        return 1/2 * (self.base_a + self.base_b) * self.height

    def __str__(self):
        return f'Площадь трапеции равна: {self.area()}'


if __name__ == '__main__':
    rectangle = Rectangle(5, 7)
    circle = Circle(6)
    right_triangle = RightTriangle(7, 8)
    trapezoid = Trapezoid(3, 5, 7)

    for figure in (rectangle, circle, right_triangle, trapezoid):
        print(figure.__str__())
print()

# Task 2
class Rectangle1(Rectangle):
    def __int__(self):
        return round(self.area())

    def __str__(self):
        return f'прямоугольника'


class Circle1(Circle):
    def __int__(self):
        return round(self.area())

    def __str__(self):
        return f'круга'


class RightTriangle1(RightTriangle):
    def __int__(self):
        return round(self.area())

    def __str__(self):
        return f'прямоугольного треугольника'


class Trapezoid1(Trapezoid):
    def __int__(self):
        return round(self.area())

    def __str__(self):
        return f'трапеции'


if __name__ == '__main__':
    rectangle = Rectangle1(5, 7)
    circle = Circle1(6)
    right_triangle = RightTriangle1(7, 8)
    trapezoid = Trapezoid1(3, 5, 7)

    for figure in (rectangle, circle, right_triangle, trapezoid):
        print(f'Площадь {figure.__str__()} рана {figure.__int__()}')

print()
# Task 3

class Shape(ABC):
    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def load(self):
        pass


class Square(Shape):
    def __init__(self, x=2, y=3, a=5):
        self.a = a
        self.x = x
        self.y = y

    def show(self):
        return 'Квадрат'

    def save(self):
        with open('figure.txt', 'a') as file:
            file.write(f'Координаты верхнего левого угла {self.x, self.y} и длина стороны {self.a}\n')

    def load(self):
        with open('figure.txt', 'r') as file:
            print(file.readlines())


class Rectangle(Shape):
    def __init__(self, x=2, y=3, a=5, b=7):
        self.a = a
        self.b = b
        self.x = x
        self.y = y

    def show(self):
        return 'Прямоугольник'

    def save(self):
        with open('figure.txt', 'a') as file:
            file.write(f'Координаты верхнего левого угла {self.x, self.y} и длина сторон {self.a, self.b}\n')

    def load(self):
        with open('figure.txt', 'r') as file:
            print(file.readlines())


class Circle(Shape):
    def __init__(self, x=2, y=3, r=4):
        self.r = r
        self.x = x
        self.y = y

    def show(self):
        return 'Круг'

    def save(self):
        with open('figure.txt', 'a') as file:
            file.write(f'Координаты центра {self.x, self.y} и радиус {self.r}\n')

    def load(self):
        with open('figure.txt', 'r') as file:
            return file.readline()


if __name__ == '__main__':
    square1 = Square()
    rectangle1 = Rectangle()
    circle1 = Circle()

    with open('figure.txt', 'w') as file:
        pass

    li = []

    for figure in [square1, rectangle1, circle1]:
        print(figure.show())
        figure.save()
    print(li)

