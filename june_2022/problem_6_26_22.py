'''
Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 
(but also not 0-100 or 100-0). You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.
'''
from random import random

def toss_biased():
    val = random()
    if val < 0.46:
        return True
    return False


'''
Taking two coin tosses:

Using Bayes
P(Coin 1 is H | Coins are opposite) = P(Coins are opposite | Coin 1 is H) P(Coin 1 is H) / P(Coins are opposite)
= (1-p)p/(2p(1-p))
= 1/2

Therefore to solve we take the result of an initial coin toss given that the coins are opposite
'''
def toss_unbiased():
    t1 = toss_biased
    t2 = toss_biased

    while t1 == t2:
        t1 = toss_biased
        t2 = toss_biased

    return t1
