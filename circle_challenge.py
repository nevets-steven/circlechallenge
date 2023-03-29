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
class Validator:
    def valid(radius_input):
        try:
            float(radius_input)
            return True
        except ValueError:
            return False


    ##validation
radius_input = input('Enter the radius of your circle: ')
if Validator.valid(radius_input) == True:
    radius_input = float(radius_input)
    circle = Circle(radius_input)
    print(f'Diameter: {circle.calculate_diameter()}')
    print(f'Circumference: {circle.circumference()}')
    print(f'Area: {circle.calculate_area()}')
    while switch == True:
        grow = input('Would you like your circle to grow? (y/n) ').lower()
        if grow == 'y':
            circle.grow()
            print('Standby while your circle magically grows...')
            print(f'Diameter: {circle.calculate_diameter()}')
            print(f'Circumference: {circle.circumference()}')
            print(f'Area: {circle.calculate_area()}')
        elif grow != 'y' and grow != 'n':
            print('Please enter "y" or "n".')
        else:
            print("Goodbye! <END PROGRAM>")
            break
else:
    print('Please enter a positive number.')


