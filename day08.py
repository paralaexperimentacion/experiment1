#importing sqrt function
from math import sqrt


#snippet one: say_hello
def say_hello():
    """Prints hello"""
    print("Hello, person!")

#print hello
say_hello()


#snippet two: fifty
def fifty():
    """Returns 50"""
    return(50)

# should print 100
print(fifty() * 2)


#snippet three: add_them_all
def add_them_all(n1, n2, n3, n4, n5):
    """Returns sum of five numbers"""
    sum = n1 + n2 + n3 + n4 + n5
    return(sum)

#:DDDD I got it
#should print 111
print(add_them_all(1, 3, 5, 2, 100))


#function to find hypotenuse
def find_hypotenuse(a, b):
    """finds the hypotenuse of triangle with sides a and b"""
    base = a * a + b * b
    return(sqrt(base))

#:DDDD whoooooooo
#should print hypotenuse
print(find_hypotenuse(5, 5))