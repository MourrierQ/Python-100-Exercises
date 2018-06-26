#Write a program which accepts a sequence of comma-separated numbers from console
# and generate a list and a tuple which contains every number.
#Suppose the following input is supplied to the program:
#34,67,55,33,12,98
#Then, the output should be:
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')

user_input = input("Please enter a comma separated sequence of integer : ")

list_res = [i for i in user_input.split(",")]
tuple_res = tuple(list_res)


print(list_res)
print(tuple_res)