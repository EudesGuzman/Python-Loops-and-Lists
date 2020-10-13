people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    newList =[]
    #Your code go here:
    for name in people:
        if person_name != name:
            newList.append(name)

    return newList

print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))