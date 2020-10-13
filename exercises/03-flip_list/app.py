arr = [45, 67, 87, 23, 5,  32, 60]

#your code below:
new_list =[]

for i in range(len(arr),0, -1):

    new_list.append(arr[i-1])

print(new_list)