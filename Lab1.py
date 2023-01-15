class Worker():
    def init(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay
        print("Работник создан")

Rabotyaga_name = []
Rabotyaga_age = []
Rabotyaga_pay = []
A = 1
while (A != 0):
    print("Что вы хотите сделать?")
    print("1 - добавить работника")
    print("2 - уволить работника")
    print("3 - редактировать работника")
    print("4 - вывести список работников")
    print("0 - закончить")
    A = int(input())
    if (A > 4 and A != 0):
        print("Не та циферка")
    if (A == 0):
        break
    if (A == 1):
        print("Введите ФИО работника")
        name1 = input()
        print("Введите возраст работника")
        age1 = input()
        print("Введите зп работника")
        pay1 = input()
        rab = Worker(name1, age1, pay1)
        Rabotyaga_name.append(rab.name)
        Rabotyaga_age.append(rab.age)
        Rabotyaga_pay.append(rab.pay)
        print("Проверьте правильность данных:\n"
              " Имя: " + rab.name +
              "\n Возраст: " + rab.age +
              "\n Заработная плата: " + rab.pay)
        print("Ваш персонал: " + str(Rabotyaga_name) + "\n")
    if (A == 2):
        if not Rabotyaga_name:
            print("У вас нет сотрудников :(\n ")
        else:
            print("Напишите номер сотрудника для увольнения)")
            print(Rabotyaga_name)
            delete = int(input())
            delete -= 1
            del Rabotyaga_name[delete]
            del Rabotyaga_age[delete]
            del Rabotyaga_pay[delete]
            print("Ваш персонал: " + str(Rabotyaga_name) + "\n")
    if (A == 3):
        if not Rabotyaga_name:
            print("У вас нет сотрудников :(\n ")
        else:
            print("Напишите номер сотрудника для редактирования")
            print(Rabotyaga_name)
            redactor = int(input())
            redactor = redactor - 1
            print("выберите какие данные хотите отредактировать: Фио - 1, Возраст - 2, зарплата - 3"
                  "\nвведите число от 1 до 3")
            t = int(input())
            if t == 1:
                print("Введите новое Фио")
                Rabotyaga_name[redactor] = input()
                print("Фио успешно изменено")
            if t == 2:
                print("Введите новый возраст")
                Rabotyaga_age[redactor] = input()
                print("Возраст успешно изменен")
            if t == 3:
                print("Введите новую зарплату")
                Rabotyaga_pay[redactor] = input()
                print("Зарплата успешно изменена")


    if (A == 4):
        if not Rabotyaga_name:
            print("У вас нет сотрудников :(\n ")
        else:
            i = 0
            while i < len(Rabotyaga_name):
                b = i + 1
                print("Работник №" + str(b) + " Имя: " + Rabotyaga_name[i] + " Возраст: " + Rabotyaga_age[i] + " Заработная плата: " + Rabotyaga_pay[i])
                i += 1