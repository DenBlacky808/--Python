class Cell:
    def __init__(self, population):
        self.population = population

    def __add__(self, other):
        return self.population + other.population

    def __sub__(self, other):
        if self.population >= other.population:
            return self.population - other.population
        else:
            return 'Ячеек в первой клетке меньше чем во второй!'

    def __mul__(self, other):
        return Cell(self.population * other.population)

    def __truediv__(self, other):
        return Cell(self.population // other.population)

    def make_order(self, raw):
        num = self.population // raw
        return print('\n'.join([(''.join(['*' for _ in range(raw)])) for _ in range(num)]) + '\n' + ''.join(
            ['*' for _ in range(self.population - num * raw)]))


cells_1 = Cell(13)
cells_2 = Cell(25)
print(cells_1 + cells_2)
print(cells_1 - cells_2)
print(cells_2 - cells_1)
cells_3 = cells_1 * cells_2
cells_4 = cells_2 / cells_1
print(cells_3.population)
print(cells_4.population)
cells_2.make_order(7)
