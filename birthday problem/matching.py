#matching problem
import random

#returns true if there are exactly "matches" matches after shuffling n cards
def match(matches,n=10):
    cards = list(range(n))
    random.shuffle(cards)
    count = 0
    for i in range(n):
        if i == cards[i]:
            count +=1
    return count == matches
