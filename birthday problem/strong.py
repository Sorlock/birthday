#strong birthday
import random

#returns true if everybody has a shared birthday
def allshared(n):
    birthdays = [0] * 365
    for i in range(n):
        birthday = random.randrange(0,364)
        birthdays[birthday] += 1
    return not 1 in birthdays
