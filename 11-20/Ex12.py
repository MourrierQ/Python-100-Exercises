#Write a program, which will find all such numbers between 1000 and 3000 (both included)
# such that each digit of the number is an even number.
#The numbers obtained should be printed in a comma-separated sequence on a single line.


res = []

for i in range(1000, 3001):
    check = True
    digits = [int(d) for d in str(i)]

    for digit in digits:
        if not digit % 2 == 0:
            check = False
    if check:
        res.append(str(i))


print(",".join(res))