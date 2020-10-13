my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]


#Your code go from here:
maxNumber= 0
for number in my_list:
    
    if number > maxNumber:
        print(number)
        maxNumber = number

print(maxNumber)