# page 11

def writeName(fname, lname):
    fullname = fname + " " + lname
    return fullname


fname = input('Enter your firstname : ')
lname = input('Enter your lastname : ')

print("Your name is", writeName(fname, lname))
