    # Bubble sort
my_list = [] #assign empty list
swapped = True # needed to enter while-loop
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: ")) #accept list elments
    my_list.append(val) # append elements to list

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted: ", my_list)
