theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:

newList =[]
def change(x):

    if x == 1:
        return "wiki"
    else:
        return "woko"



result = list(map(change, theBools))
print(result)
