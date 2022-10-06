'''
Given a list of words, return the shortest unique prefix of each word.
For example:

['dog', 'cat', 'apple', 'apricot', 'fish']

would return

['d', 'c', 'app', 'apr', 'f']
'''


#Cases

#First letter eg ['dog', 'cat', 'fish'] -> ['d', 'c', 'f']
#First few eg ['apricot', 'apple'] -> ['apr', 'app']
#Full eg 'fish' in ['fish', 'fisherman'] -> ['fish', 'fishe']
#Full + 1 eg 'fisherman' in ['fish', 'fisherman'] -> ['fish', 'fishe']

def short_pref(arr):
    prefixes = []
    for i in range(len(arr)):
        cur = arr[i]
        prefix = cur[0]
        for j in range(len(arr)):
            if i == j:
                continue
            compared = arr[j]
            match = False
            for z in range(1, min(len(cur), len(compared))):
                if cur[z] == compared[z]:
                    prefix += cur[z]
                    match = True
                else:
                    break

            if match and z < len(cur) - 1:
                prefix += cur[z+1]

        prefixes.append(prefix)
    return prefixes

print(short_pref(['dog', 'cat', 'apple', 'apricot', 'fish', 'fisher']))

