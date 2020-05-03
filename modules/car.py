class Car:
    color = ''
    speed = 0
    car_on = False

    def __init__(self, color):
        self.color = color

    def is_car_on(self):
        if self.car_on:
            return 'yes'
        else:
            return 'no'

    def is_car_moving(self):
        if self.speed > 0:
            return 'Car is moving {} MPH.'.format(self.speed)
        else:
            return 'Car is not moving'

    def set_car_color(self, color):
        self.color = color

    def get_car_spec(self):
        print('Cars color is {}'.format(self.color))
        print('Cars speed is {}'.format(self.speed))
        print('Is car on? {}'.format(self.is_car_on()))
        print(self.is_car_moving())

    def turn_car_on(self):
        self.car_on = True
        print('Car is now on');

    def move_car(self):
        self.speed += 1
        print('Car is now moving at {} MPH'.format(self.speed))
