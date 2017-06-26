#This is a Python script that, for a given list of strings(variables), will
#create all the possible permutations of products, including own and cross
#products.
separator = "*";
VarList = ["y","lp","ep","rmp","cmp","cp","fp"]
n = len(VarList)
r = 2

newVarList = [];

currPosition = 0
for currVar in VarList:
    currPosition +=1
    nextPosition = 0
    for nextVar in VarList:
        nextPosition+=1
        if currPosition <= nextPosition:
            currText = currVar + separator + nextVar
            if currText not in newVarList:
                newVarList.append(currText)

#Check the number of combinations os correct, should equate to (n!/(r!(n-r)!)+n)
# the added n is for squares of the variable.
import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return ((numer//denom)+n)

possible = ncr(n,r)
print possible
actual = len(newVarList)
print actual

actual == possible
print((' '.join(map(str, newVarList))))
