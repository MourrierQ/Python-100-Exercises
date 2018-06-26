#Define a class which has at least two methods:
#    getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include simple test function to test the class methods.

class Printer():


    def getString(self, inp):
        self.user_input = inp

    
    def printString(self):
        print(self.user_input.upper())


my_printer = Printer()
my_printer.getString(input("Please enter a string : "))

my_printer.printString()