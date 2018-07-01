#Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
#Suppose the following input is supplied to the program:
#9
#Then, the output should be:
#11106

import math

def addNums(x, n):
    numbers = [x]
    i = 1
    while i < n:
        seq = [str(x)]
        j = 1
        while j <= i:
            seq.append(str(x))
            j += 1
        numbers.append(int("".join(seq)))
        i += 1
    print(numbers)
    print(sum(numbers))


addNums(9, 4)




