#Write a program that accepts a sentence and calculate the number of letters and digits.
#Suppose the following input is supplied to the program:
#hello world! 123
#Then, the output should be:
#LETTERS 10
#DIGITS 3

letters = 0
digits = 0

user_input = input("Please enter a sentence : ").replace(" ", "")

for i in user_input:
    if i.isdigit():
        digits += 1
    else:
        if i.isalpha():
            letters += 1

print("LETTERS {}".format(letters))
print("DIGITS {}".format(digits))


