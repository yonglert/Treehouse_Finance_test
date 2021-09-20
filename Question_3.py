'''
    Each number on the Pascal's triangle is a number combination of N take r.
    N is the row number starting from 0; r is the nth number of row N, starting from 0

    1               0C0
    1 1         ->  1C0  1C1
    1 2 1           2C0  2C1  2C2
    1 3 3 1         3C0  3C1  3C2  3C3
    ..........

    NCr formula: N! / [(N-r)!*r!]

    Write function createPascal(N) which takes N rows
    for each row, (start from 0 to N-1)
        for each number,r, (there is 1 to N inclusive numbers)
            print each value of NCr and add end=" " to add a space between each number
        
        print() to start printing on new line for next row
    ------------------------------------------------------------------------------------------
    Runtime: O(N^2)
'''
from math import factorial

def createPascal(N):
    for row in range(N):
        for k in range(row+1):
            # Use floor division so that it will not return float
            print(factorial(row) // (factorial(k) * factorial(row-k)), end = " ")
        print() # print on new line

# Test with N = 6
createPascal(6)