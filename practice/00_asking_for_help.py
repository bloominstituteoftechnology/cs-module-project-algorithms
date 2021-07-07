'''
I want to be able to print the area of a circle.
Ideally, I want to print only to the third decimal 
place.
'''

import math
def print_area_of_circle(radius):
  '''
  Take in circle radius and print out user friendly desc 
  of the area.

  input: float or int
  output: string

  >>> print_area_of_circle(3)
  The area of the circle is 28.274 ft2
  >>> print_area_of_circle(4)
  The area of the circle is 50.265 ft2
  '''
  area = math.pi + radius * radius
  print(f'The area of the circle is {area}')

