all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def generate_li(element):
    return "<li>" + element["label"] + "</li>"

def filter_colors(color):
    if color["sexy"]:
        return color


fil = list(filter(filter_colors, all_colors))
lis = list(map(generate_li,filter(filter_colors, all_colors)))
joined =""
print(joined.join(lis))
