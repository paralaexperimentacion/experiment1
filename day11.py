#while loop 1
tru_num = int(input("What is the best number from 1-10?: "))

while tru_num != 3:
    tru_num = int(input("I'm sorry, but that is simply untrue. Try again: "))

if tru_num == 3:
    print("You are correct!")


#while loop 2 + 3
print("Lists all values of a number 'x to the xth power' until the value exceeds 10,000,000,000.")

x = int(input("Give a number 'x' from 1-10: "))

print(f"The number that you selected was {x}.")

while x <= 0 or x > 10:
    x = int(input("I'm sorry, but that number is unacceptable. Please insert another number from 1 to 10: "))

x1 = x ** x

while x1 <= 10000000000:
    print(x1)
    x1 = x1 ** x1

if x1 >= 10000000000:
    print("Here are all the values. You may notice that there are not as many as you think there would've been.")

#while loop 4 + 5
tru_name = "Kathryn"
tru_name2 = "Kat"

while tru_name == "Kathryn":
    name = input("What is your favorite name?: ")
    print(f"You chose the name {name}.")
    if name == tru_name or name == tru_name2:
        print("That is true, it is only the best name.")
        break
    while name != tru_name or name != tru_name2:
        name = input("I'm sorry that you are incorrect. I will give you another chance to choose a name: ")
        if name == tru_name or name == tru_name2:
            print("That is true, it is only the best name.")
            break
        number = int(input("How many times have you had to choose a name?: "))
        if number >= 10:
            exit = input("I'm sorry that you had to choose so many times. If you would like to stop trying to be correct, type in 'no': ")
            if exit == "no" or exit == "NO" or exit == "No":
                print("You will now no longer have to choose. By the way, the answer was Kathryn or Kat.")
                break
            if exit != "no":
                name = input("Choose another name: ")
                break
            break
        break
    break
