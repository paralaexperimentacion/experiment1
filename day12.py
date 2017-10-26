#defines the starting point, x
x = 0

#while loop
while x <= 10000:
    #makes sure that x increase by one each time it loops
    x = x + 1
    #prints the number if x is not divisble by anything
    if x % 3 != 0 and x % 11 != 0 and x != 10001:
        print(f"{x}")
    #prints the word "motorcycle" if x is divisible by both three and eleven
    if x % 3 == 0 and x % 11 == 0:
        print("motorcycle")
    #prints the word "bicycle" if x is divisible by three, but not eleven
    elif x % 3 == 0:
        print("bicycle")
    #prints the word "car" if x is divisible by eleven, but not three
    elif x % 11 == 0:
        print("car")

#prints that everything is completed
print("Finished!")