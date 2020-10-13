import random
# Create the function below:

lis = []
lis2=[]
def matrixBuilder(num):
    for i in range(num):
        lis.append(1)
    for k in range(num):
        lis2.append(lis)
    return lis2
print(matrixBuilder(random.randint(2,5)))




