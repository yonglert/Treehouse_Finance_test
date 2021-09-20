''' 
    Python would not be able to run if there is uninitialized variables, it will throw a NameError
    exeption during runtime and hence the function "exists" would not be called.

    solution:
        Use Try-Except to catch NameError (undefined variables)
        If NameError exception is raised: set the variable to None then pass into function "exists"
        Then using the function to print result whether the variable is defined or undefined.
'''

def exists(v):
    if v is None:
        print("Variable does not exist")
    else:
        print("Variable exists")

##################################################################################################
'''
    Case 1: v does not exists
    How to duplicate: Do not initialize v, run try-except block to test
    Result: Print "Variable does not exist
'''
try:
    v
except NameError: # Catch the NameError exception which is raised when a variable is undefined
    v = None      # Set v as None
    exists(v)     # call function "exists"
else:
    exists(v)     # v exists -> call function "exists"

##################################################################################################
'''
    Case 2: v exists
    How to duplicate: Initialize v and run try-except block again
    Result: Print "Variable exists"
'''
v = 0 # Can be initialized as a string, integer, float, or any object
try:
    v
except NameError:
    v = None
    exists(v)
else:
    exists(v)