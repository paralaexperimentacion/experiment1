#assigning variables
#also using inputs in order to get user's choice
animal_1 = input("animal: ")
animal_2 = input("animal: ")
name_1 = input("name: ")
name_2 = input("name: ")
adjective_1 = input("adjective: ")
adjective_2 = input("adjective: ")
adjective_3 = input("adjective: ")
adjective_4 = input("adjective: ")
familial_relation_1 = input("familial relation: ")
familial_relation_2 = input("familial relation: ")
job_1 = input("occupation: ")
job_2 = input("occupation: ")
verb_1 = input("-ing verb: ")
verb_2 = input("present tense verb: ")
verb_3 = input("present tense verb: ")

#story
string = """Once upon a time, there was a {0} named {2}.
{2} was {4} and {5}, but he had a good, steady, income with his occupation as an {10}.
He was best friends with a {6} {1} called {3}.
They both believed that they were {8}s, or so {2} thought.
One {7} day, {2} was {12} with a {11} when he discovered that {3} was following him.
{3} tried to {13}, but {2} wouldn't {14}.
In the end, {2} the {0} discovered that {3} the {1} was not his {8} but was actually his {9}!"""

#printing story
print(string.format(animal_1, animal_2, name_1, name_2, adjective_1, adjective_2, adjective_3, adjective_4, familial_relation_1, familial_relation_2, job_1, job_2, verb_1, verb_2, verb_3))