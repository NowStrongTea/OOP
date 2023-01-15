class Figure(ABC):
    def __init__(self):
        self.square = 'Площадь = xxx'
        self.perimeter = 'Периметр = yyy'
        print(self.square, self.perimeter)


# Площадь и периемтр треугольника
class Triangle(Figure):
    def __init__(self, a, b, c):
        self.name = 'треугольник'
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return (self.a + self.b + self.c)

    def square(self):
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


# Площадь и периметр круга
class Circle(Figure):
    def __init__(self, r):
        self.name = 'круг'
        self.r = r

    def perimeter(self):
        return 2 * 3.14 * self.r

    def square(self):
        return 3.14 * (self.r ** 2)


# Площадь и периметр четырёхугольника
class Quadrilateral(Figure):
    def __init__(self, a, b):
        self.name = 'четырехугольник'
        self.a = a
        self.b = b

    def perimeter(self):
        return (self.a + self.b) * 2

    def square(self):
        return self.a * self.b


# Координаты класса 'Точка'
class Point():
    def g_point(self, x, y):
        self.x = x
        self.y = y
        data = [self.x, self.y]
        return data

    def show(self):
        return 'Координаты: x = {}, y = {}'.format(self.x, self.y)


# Класс "Сторона"
class Side(Point):
    def g_side(self, xy1, xy2):
        self.x1, self.y1 = xy1[0], xy1[1]
        self.x2, self.y2 = xy2[0], xy2[1]

        side = abs(sqrt((self.y2 - self.y1) ** 2 + (self.x2 - self.x1) ** 2))
        return int(side)


p = Point()
s = Side()

figure_amount = int(input('Напишите количество фигур '))

figure_dict = {}
for i in range(figure_amount):
    figure_type = input('Площадь какой фигру вы хотите посчитать? (треугольник, круг, четырехугольник) ').lower()
    if figure_type == 'треугольник':
        x_1 = int(input('х1: '))
        y_1 = int(input('y1: '))
        x_2 = int(input('х2: '))
        y_2 = int(input('y2: '))
        x_3 = int(input('х3: '))
        y_3 = int(input('y3: '))
        t = Triangle(s.g_side(p.g_point(x_1, y_1), p.g_point(x_2, y_2)),
                     s.g_side(p.g_point(x_2, y_2), p.g_point(x_3, y_3)), s.g_side(p.g_point(x_3, y_3)),
                     p.g_point(x_1, y_1))
        key, value = t.name, t.square()
        figure_dict[key] = value
    elif figure_type == 'круг':
        x_1 = int(input('х1: '))
        y_1 = int(input('y1: '))
        x_2 = int(input('х2: '))
        y_2 = int(input('y2: '))
        c = Circle(s.g_side(p.g_point(x_1, y_1), p.g_point(x_2, y_2)))
        key, value = c.name, c.square()
        figure_dict[key] = value
    elif figure_type == 'четырехугольник':
        x_1 = int(input('х1: '))
        y_1 = int(input('y1: '))
        x_2 = int(input('х2: '))
        y_2 = int(input('y2: '))
        x_3 = int(input('х3: '))
        y_3 = int(input('y3: '))
        x_4 = int(input('х4: '))
        y_4 = int(input('y4: '))
        q = Quadrilateral(s.g_side(p.g_point(x_1, y_1), p.g_point(x_2, y_2)),
                          s.g_side(p.g_point(x_2, y_2), p.g_point(x_3, y_3)), s.g_side(p.g_point(x_3, y_3)),
                          p.g_point(x_4, y_4), s.g_side(p.g_point(x_4, y_4)), p.g_point(x_1, y_1))
        key, value = q.name, q.square()
        figure_dict[key] = value

figure_dict = dict(sorted(figure_dict.items(), reverse=True, key=lambda x: x[1]))

my_table = PrettyTable()
my_table.field_names = ["Имя", "Площадь"]

for i in figure_dict:
    my_table.add_row([i, figure_dict[i]])

print(my_table)