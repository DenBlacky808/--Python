import itertools
import time


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green', 'Yellow']

    def working(self, num):
        for value in itertools.cycle(self.__color):
            if num < 0:
                break
            elif value == 'Red':
                print("\033[31m {}".format('Red'))
                time.sleep(7)
            elif value == 'Yellow':
                print("\033[33m {}".format('Yellow'))
                time.sleep(2)
            elif value == 'Green':
                print("\033[32m {}".format('Green'))
                time.sleep(5)
            num -= 1


new_one = TrafficLight()
new_one.working(5)
