#Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
#Suppose the following input is supplied to the program:
#Hello world!
#Then, the output should be:
#UPPER CASE 1
#LOWER CASE 9

upper = 0
lower = 0

user_input = input("Please enter a sentence : ").replace(" ", "")

for i in user_input:
    if i.isupper():
        upper += 1
    else:
        if i.islower():
            lower += 1


print("UPPER CASE {}".format(upper))
print("LOWER CASE {}".format(lower))