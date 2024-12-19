print('Задача "История строительства":')
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".
# В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.
# Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.
# Дополните метод __new__ так, чтобы:
# Название объекта добавлялось в список cls.houses_history.
# Название строения можно взять из args по индексу.
# Также переопределите метод __del__(self) в котором будет выводиться строка:
# "<название> снесён, но он останется в истории"
# Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также значение атрибута houses_history.
# Домашняя работа по уроку "Перегрузка операторов"
print('Задача "Нужно больше этажей":')
# Необходимо дополнить класс House следующими специальными методами:
class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)  # Создаем новый объект с использованием super().__new__(cls)
        cls.houses_history.append(args[0])  # Добавляем название в список истории
        return instance
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if self.number_of_floors < new_floor or  new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(new_floor+1):
                print(i)
                # Необходимо дополнить класс House следующими специальными методами:
# __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
    def __len__(self):
        return self.number_of_floors
    # __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"
# __eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
# Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
# __add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
# __radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
# Остальные методы арифметических операторов, где self - x, other - y:
    def __eq__(self,other): # (==)
        return self.number_of_floors == other.number_of_floors
    def __lt__(self,other): # (<)
        return self.number_of_floors < other.number_of_floors
    def __le__(self,other): # (<=)
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self,other): # (>)
        return self.number_of_floors > other.number_of_floors
    def __ge__(self,other): # (>=)
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self,other): # (!=)
        return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        elif isinstance(value, House):
            return House(self.name, self.number_of_floors + value.number_of_floors)
        else:
            raise TypeError("__add__ не поддерживает сложение с объектами типа 'value'")

    def __radd__(self, value):
        return self.__add__(value)  # Используем метод __add__

    def __iadd__(self, value):
        self.number_of_floors += value
        return self
    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")
# Пример выполнения программы:
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
# Удаление объектов
del h2
del h3
print(House.houses_history)
