'''
Program to test out addition and multiplication functionalitvar_y

Methods
-------
    add(var_x,var_y):
        Returns the sum of two numbers
    distribute(var_x,var_y,var_z):
        Returns (var_x+var_y) * var_z
'''
# To add a new cell, tvar_ype '# %%'
# To add a new markdown cell, tvar_ype '# %% [markdown]'
# %%
def add(var_x,var_y):
    '''Takes in two numbers, returns their sum'''
    print("var_x=",var_x,"var_y=",var_y,"var_x+var_y=",var_x+var_y)
    return var_x + var_y

def distribute(var_x,var_y,var_z):
    '''Takes in three numbers, returns (var_x+var_y) * var_z'''
    print("var_x=",var_x,"var_y=",var_y,"var_z=",var_z)
    var_product = var_z * add(var_x,var_y)
    print("var_product=",var_product)
    return var_product

print("hello world")
TOTAL = add(100,5)
PRODUCT = distribute(5,10,3)
print((TOTAL+PRODUCT))

# %%
distribute(5,4,34)
add(66,33)

# %%
add(8,9)
