# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
def double(x):
    doubled_x = x * 2
    return doubled_x

four_doubled = double(4)
print(four_doubled)


def initials(name):
    first = name[0].upper()
    last = name[name.find(' ')+1].upper()
    return f'{first}. {last}.'

test = initials('Ex Ample')
test2 = initials('Bob Cat')
test3 =initials('Function Nice')

print( test, test2, test3)


# exercise
def greet(name):
    return f'Hello, {name}!'
testbob = greet('Bob')
print(testbob)

def add(x,y,z):
    return x+y+z
testing = add(2,3,5)
print(testing)

def positive(number):
    return bool(number)
eerste = positive(50)
tweede = positive(-50)
derde = positive(0)
print(eerste,tweede,derde)

def negative(numbers):
    return not bool(numbers)
vierde = negative(50)
vijfde = negative(-50)
zesde = negative(0)
print(vierde,vijfde,zesde)
