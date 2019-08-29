name = raw_input("WHAT IS YOUR NAME?\n")

def greet(name):
    greeting = "HELLO, " + name.upper() + "!"
    print(greeting + "\nYOUR NAME HAS " + str(len(name)) + " LETTERS IN IT! AWESOME!")

greet(name)