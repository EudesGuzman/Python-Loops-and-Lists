
spanish_translations = { "dog": "perro", "house": "casa", "cat": "gato" }

def myfunc(text1,text2):
    spanish_translations[text1]=text2


myfunc("love","amor")
myfunc("code","codigo")
myfunc("smart","inteligente")


print("Translation", spanish_translations["dog"])
print("All", spanish_translations)

