'''
Given a string and a set of characters, return the shortest substring containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, return null.
'''

'''
NOT DONE NOT DONE NOT DONE NOT DONE NOT DONE NOT DONE NOT DONE 
'''

mystring = "figehaeci"
chars = {'a', 'e', 'i'}

def substring(mystring, chars):
    locs = []
    ran = 0
    for x in chars:
        if x in mystring:
            my_locs = []
            for i, char in enumerate(mystring):
                if x == char:
                    my_locs.append(i)
                    if len(my_locs) > ran:
                        ran = len(my_locs)
            locs.append(my_locs)
        else:
            return None
    combs = []
    for i in range(len(locs)):
        for j in range(locs[i]):
            pass
    return locs, ran

print(substring(mystring, chars))

for x, i in enumerate("chase"):
    print(x, i)