from abc import ABC, abstractmethod


class Singleton():
    __insatance = None

    def __new__(cls, *args, **kwargs):
        if cls.__insatance is None:
            cls.__insatance = super(Singleton, cls).__new__(cls)

        return cls.__insatance


class AbstractMachine(Singleton):
    @abstractmethod
    def __init__(self):
        pass


class Robot(AbstractMachine):
    def __init__(self, name, num):
        self.name = name
        self.num = num


class Decorator(AbstractMachine):
    def __init__(self, decorate):
        self._decorate = decorate


class LearningDecorator(Decorator):

    def __init__(self, decorate):
        self._decorate = decorate
        self.name = decorate.name
        self.num = decorate.num

    def build_a_house(self):
        print('построить дом...')

    def build_a_barn(self):
        print('построить сарай...')


class WorkingDecorator(Decorator):

    def __init__(self, decorate):
        self._decorate = decorate
        self.name = decorate.name
        self.num = decorate.num

    def add_a_floor(self):
        print('добавить этаж...')

    def demolish_the_top_floor(self):
        print('снести верхний этаж...')

    def build_a_house(self):
        self._decorate.build_a_house()

    def build_a_barn(self):
        self._decorate.build_a_barn()


def represent(rob):
    print('\nПривет, я {0}, меня зовут {1}'.format(rob.name, rob.num))


robot_0 = Robot('В', "АА001221-56")
represent(robot_0)
robot_1 = LearningDecorator(robot_0)
robot_1.name = 'ВИТА'
represent(robot_1)
robot_1.build_a_barn()
robot_1.build_a_house()

robot_2 = WorkingDecorator(robot_1)
robot_2.name = 'Виталий'
represent(robot_2)
robot_2.build_a_barn()
robot_2.build_a_house()
robot_2.add_a_floor()
robot_2.demolish_the_top_floor()
