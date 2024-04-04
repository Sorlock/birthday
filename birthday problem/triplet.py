#triplet
import random

#returns true if there are 3 people sharing the same birthday in the group of n people
def triplet(n):
    birthdays = [0] * 365
    for i in range(n):
        birthday = random.randrange(0,364)
        birthdays[birthday] += 1
    return 3 in birthdays
