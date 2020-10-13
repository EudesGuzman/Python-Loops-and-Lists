
names = ['Liam','Emma','Amoah','Olivia','William','Ava','James','Isabella','Logan','Sophia',
'Benjamin','Mia','Mason','Charlotte','Elijah','Amelia','Oliver','Evelyn','Jacob','Abigail',
'Lucas','Harper','Michael','Emily','Alexander','Elizabeth','Ethan','Avery','Daniel','Sofia',
'Matthew','Ella','Aiden','Madison','Henry','Scarlett','Joseph','Victoria','Jackson','Aria',
'Samuel','Grace','Sebastian','Chloe','David','Camila','Carter','Penelope','Wyatt','Riley']


#Your code go here:
def my_func(name):
    # if "am" in name.lower():
    if "am" in name:
        return name

result =list(filter(my_func, names))
print(result)


