par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
#your code go here:
for key in par.lower().replace(" ", ""):
    # print(key)
    if key not in counts:
        counts[key] = 1
    elif key in counts:
        counts[key] = counts[key]+1
    

print(counts)

