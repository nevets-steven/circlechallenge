## Circle Challenge

import math
#global variables
pi = math.pi
switch = True

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_diameter(self):
        return self.radius*2
    def circumference(self):
        return self.radius*2.0*pi
    def calculate_area(self):
        return (self.radius**2.0) * pi
    def grow(self):
        self.radius += 1
    def get_radius(self):
        return self.radius

while switch == True:
    ##validation
    radius = float(input('Enter the radius of your circle: '))
    try:
        circle = Circle(radius)
        print(f'Diameter: {circle.calculate_diameter()}')
        print(f'Circumference: {circle.circumference()}')
        print(f'Area: {circle.calculate_area()}')
        while switch == True:
            grow = input('Would you like your circle to grow? (y/n) ').lower()
            if grow != 'n':
                circle.grow()
                print('Standby while your circle magically grows...')
                print(f'Diameter: {circle.calculate_diameter()}')
                print(f'Circumference: {circle.circumference()}')
                print(f'Area: {circle.calculate_area()}')
            else:
                print("Goodbye! <END PROGRAM>")
                switch = False
                break

    except ValueError:
        print('Please enter a valid value.')

