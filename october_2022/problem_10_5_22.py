'''
Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome.

For example. given the list
["code", "edoc", "da", "d"],
return
[(0, 1), (1, 0), (2, 3)]
'''

def is_pal(string):
    wordlen = len(string)
    for i in range(wordlen):
        if string[i] != string[-i-1]:
            return False

        if i + i >= wordlen:
            return True

def pal_identifier(arr):
    pals =[]
    for i in range(len(arr)-1):
        cur = arr[i]
        for x in range(i, len(arr)):
            alt = arr[x]

            concat1 = cur + alt
            concat2 = alt + cur

            if is_pal(concat1):
                pals.append((i, x))
            if is_pal(concat2):
                pals.append((x,i))

    return pals

print(pal_identifier(["code", "edoc", "da", "d"]))

