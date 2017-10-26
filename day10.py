#if statement 1: favorite number
#provides description of what will happen to user
print("This will tell you how good your favorite number is.")

#defines variable/input
fav_number = int(input("What is your favorite number? (must be an integer): "))

#determines response
if fav_number != 19:
    print("I'm sorry, but you're wrong.")
if fav_number == 19:
    print("You have good taste.")



#if statement 2: age
#provides description of what will happen to user
print("This will tell you the status of your age and health.")

#defines variable/input
age = int(input("What is your age?: "))

#determines if input is acceptable or not
while age >= 130 or age <=0:
    age = int(input("That is impossible, you liar. How old are you?: "))

#defines variable/input
birthday_month = int(input("What month is your birthday? (number): "))

#determines if input is acceptable or not
while birthday_month > 12:
    birthday_month = int(input("That is impossible. What month is your bithday?: "))

#determines response
if age == 16 and birthday_month >= 5:
    print("You are in the prime of your life!")
elif age == 16 and birthday_month < 5 or age > 16 and age < 32:
    print("You practically have one foot in the grave.")
elif age > 32:
    print("Are you a vampire? I will pray for your health.")
elif age < 16 and age > 0:
    print("You are a fetus.")



#if statement 3: even or odd
#provides description of what will happen to user
print("This will tell you if the sum of two numbers is even or odd")

#defines variables/inputs
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

#calculations
num_total = num1 + num2
num_remainder = num_total % 2

#determines response
if num_remainder != 0:
    print("The sum of those numbers is odd.")
else:
    print("The sum of those numbers is even.")



#if statement 4: homework and the quality of day
print("This will tell you the quality of your day in relation to your homework.")

#defines variable/input
hw = input("Do you have homework?: ")

#determines response
if hw == "yes" or hw == "YES" or hw == "Yes":
    print("I'm sorry, your day is already awful, unless it's physics homework.")
elif hw == "no" or hw == "NO" or hw == "No":
    print("Wow, is school that easy? Your day will be great.")
else:
    print("That is not an acceptable answer. It is clear by your attitude that you are a jerk and karma will get back to you.")