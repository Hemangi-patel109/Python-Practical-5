my_tuple = {1,2,3,4,5,6,7,8,9}
search = [3,6,9]
found = []
for i in search:
    if i in my_tuple:
        found.append(i)
print("Found item: ",found)