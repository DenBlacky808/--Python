class ExceptZero(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a = list(map(int, (input('Введите делимое и делитель через пробел: ').split())))
    if a[1] == 0:
        raise ExceptZero('На ноль делить нельзя!')
    print(round(a[0] / a[1], 2))
except ExceptZero as err:
    print(err)
