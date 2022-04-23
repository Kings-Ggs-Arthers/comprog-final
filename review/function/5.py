message = "a"

def greet(name):
    global message
    message = "c"

greet("b")
print(message)
