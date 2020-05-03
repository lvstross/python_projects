#!/usr/bin/env python
from car import Car
from color import Color

def main():
    color = Color()
    van = Car(color.colors.get("black"))
    van.get_car_spec()
    van.turn_car_on()
    van.move_car();
    van.move_car();

if __name__ == '__main__': main()
