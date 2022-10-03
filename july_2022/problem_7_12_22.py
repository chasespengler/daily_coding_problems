'''
Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.
'''

'''

NOT DONE NOT DONE NOT DONE NOT DONE NOT DONE

'''

#z = open("file.txt", "r")
z = "Hello world"
t = 0

def read7():
    global t
    try:
        mystring = z[t * 7:t * 7 + 7]
    except:
        try:
            mystring = z[t * 7:]
        except:
            mystring = ""
    t += 1
    return mystring

print(read7())
print(read7())
print(read7())

def readN(n):
    before = []
    after = []

    if n < 7:
        div = 7 // n
        rem = 7 % n
        while div:
            pass
    elif n > 7:
        pass
    else:
        return read7()
