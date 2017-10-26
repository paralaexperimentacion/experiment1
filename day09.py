#imports the pi variable
from math import pi

#gets the value of radius from the user
radius = int(input("give a radius: "))

#defines function to give circumference of a circle
def find_circumference(radius):
    """provides circumference of a circle given a radius"""
    n1 = 2 * radius * (pi)
    return(n1)

#defines function to give area of a circle
def find_area(radius):
    """provides area of a circle given a radius"""
    n2 = pi * radius ** 2
    return(n2)

#defines function to give surface area of a sphere
def find_surface_area(radius):
    """provides surface area of a sphere given a radius"""
    n3 = 4 * pi * radius ** 2
    return(n3)

#prints all the results of the radius
print(f"""With a radius of {radius}:
The circumference of a circle is {find_circumference(radius)}.
The area of a circle is {find_area(radius)}.
The surface area of a sphere is {find_surface_area(radius)}.""")