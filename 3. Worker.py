class Worker:
    name = 'some_name'
    surname = 'some_surname'
    position = 'some_position'
    __income = {'wage': 1000, 'bonus': 200}


class Position(Worker):
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income

    def get_full_name(self):
        print(f'{self.name} {self.surname} {self.position}')

    def get_total_income(self):
        result = 0
        for key, value in self.__income.items():
            result += value
        return print(result)


director = Position('Alex', 'Smith', 'Director', {'wage': 100000, 'bonus': 10000})
manager = Position('Jhon', 'Stone', 'Manager', {'wage': 50000, 'bonus': 5000})
print(director.name)
print(manager.surname)
director.get_full_name()
director.get_total_income()
manager.get_full_name()
manager.get_total_income()
