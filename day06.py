#variables store types of pie
pie_1 = "raspberry"
pie_2 = "cherry"
pie_3 = "rhubarb"

#variables store quality of pie
quality_1 = "delicious"
quality_2 = "alright"
quality_3 = "gross"

#string format 1
print(f"{pie_3} pie varies in quality depending on how well it is cooked, but it is generally {quality_1}.")
print(f"{pie_2} is my least favorite type of pie.")

    #using a variable in order to print
description = f"{pie_1}, {pie_2}, and {pie_3} are all types of pies"
print(description)

#string format 2
print("My litle sister's favorite pies are {} and {}".format(pie_1, pie_2))
print("{} pies are {}, but {} pies are {}".format(pie_2, quality_3, pie_1, quality_2))

    #using numbers in order to order the variables in the brackets
print("My ranking of pies in order from most delicious to least delicious would be {2}, {0}, then {1}.".format(pie_1, pie_2, pie_3))
print("My little sister's ranking of pies from most to least delicious would be {}, {}, then {}.".format(pie_1, pie_2, pie_3))

#string format 3/reusing strings
    #text
f_string = "{} {} {}"

print(f_string.format(pie_1, pie_2, pie_3))
print(f_string.format("a", "b", "c"))
print(f_string.format(1, 2, "tres"))

    #math
math_string = "{} * {} - {}"

print(math_string.format(1, 3, 5))
print(math_string.format(16, 12, 72))
print(math_string.format(8, 2, 1))
print(math_string.format(99, 99, 99))

#string format 4/splitting lines
print("if I want to put {0} pie on a different line than {1} pie, I would do {0} pie\n{1} pie".format(pie_3, pie_1))

#string format 5/long strings
long_string = """my list of pies from best to worst would be:
rhubarb
raspberry
cherry"""

print(long_string)
