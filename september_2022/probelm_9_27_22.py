'''
Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
'''

def recur(word):
    t = []
    for x in word:
        if x not in t:
            t.append(x)
        else: return x
    
    return None