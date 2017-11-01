pumpkin = int(input("How many pumpkins are necessary for a pumpkin pie?: "))

def pie(pumpkin):
    if pumpkin <= 0:
        print("""That is not enough pumpkins!""")
    if pumpkin > 0 and pumpkin <= 1:
        print("""That is the perfect amount of pumpkins!""")
    if pumpkin > 1:
        print("""That is way too many pumpkins!""")

pie(pumpkin)