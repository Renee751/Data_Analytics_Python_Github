# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
def greet(name):
    return f'Hello, {name}!'
testbob = greet('Bob')
print(testbob)

def add(x,y,z):
    return x+y+z
testing = add(2,3,5)
print(testing)

def positive(number):
    positive_nbr = (number > 0) == True
    return positive_nbr
eerste = positive(50)
tweede = positive(-50)
derde = positive(0)
print(eerste,tweede,derde)

def negative(numbers):
    negative_nbr = (numbers < 0) == True
    return negative_nbr
vierde = negative(50)
vijfde = negative(-50)
zesde = negative(0)
print(vierde,vijfde,zesde)
