#Write a program that will convert the colors tuple to a dictionary.
#my code
colors = (("green", "#008000"), ("blue", "#0000FF"))
# Write your code here.
colors_dictionary = {}
for item in colors:
    #colors_dictionary.update(item)
    colors_dictionary.update({item[0]: item[1]})
    
print(colors_dictionary)

#instructor code
colors_dictionary = dict(colors)
print(colors_dictionary)
