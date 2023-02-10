'''File to test out Python methods'''

print("This is my new file! yipee!!!")
print("you are a master Python Jedi")
print('and you are a good bash user')

def add(x,y):
    'adds two numbers together'
    return x+y

def multiply(x,y):
    'multiplies two numbers together'
    return x*y

def distribute(x,y,z):
    'returns x*(y+z)'
    return x*(y+z)

def exponentiate(x,y):
    'raises x to the y power'
    return x^y

SUM = add(10,5)
PRODUCT = multiply(3,6)
TOTAL = distribute(5, SUM, PRODUCT)
print("Total:",TOTAL)

TOTAL = 5555
print("New total:",TOTAL)



