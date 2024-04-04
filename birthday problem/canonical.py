#canonical birthday
import random

#returns true if two people have the same birthday out of n people, false otherwise
def duplicate(n):
    birthdays = []
    for i in range(n):
        birthday = random.randrange(1,365)
        if birthday in birthdays:
            return True
        birthdays.append(birthday)
    return False
