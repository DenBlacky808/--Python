class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, side):
        if side == 'right':
            print(f'{self.name} повернула направо')
        else:
            print(f'{self.name} повернула налево')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Скорость превышена!')
        print(self.speed)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Скорость превышена!')
        print(self.speed)


class PoliceCar(Car):
    pass


class SportCar(Car):
    pass


plc_car = PoliceCar(70, 'Blue', 'Lada', True)
sprt_car = SportCar(110, 'Red', 'Lambo', False)
wrk_car = WorkCar(70, 'White', 'Toyota', False)
twn_car = TownCar(50, 'Grey', 'Mazda', False)
print(sprt_car.speed)
print(plc_car.color)
print(wrk_car.name)
plc_car.go()
wrk_car.stop()
twn_car.turn('left')
twn_car.show_speed()
wrk_car.show_speed()
