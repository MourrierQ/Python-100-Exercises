# Question:
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

# Hints:
# Consider use yield

class GenClass():

    @staticmethod
    def generator(n):
        for i in range(0,n+1):
            if i % 7 == 0:
                yield i

out = GenClass.generator(100)

for g in out:
    print(g)