#assigning variables
animal_1 = "unicorn"
animal_2 = "narwhal"
name_1 = "Alabaster"
name_2 = "Nostradomus"
adjective_1 = "ugly"
adjective_2 = "dumb"
adjective_3 = "clever"
adjective_4 = "fine"
familial_relation_1 = "cousin"
familial_relation_2 = "long-lost twin brother"
job_1 = "assassin"
job_2 = "lumberjack"
verb_1 = "hunting"
verb_2 = "explain"
verb_3 = "listen"

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