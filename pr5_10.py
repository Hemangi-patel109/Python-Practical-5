def check_exist(dic,key):
    if key in dic:
        return True
    else:
        return False
my_disc = {'name': 'Hemangi', 'age': 21, 'class': '6D'}
key_search = 'age'
if check_exist(my_disc,key_search):
    print(f"Key {key_search} is in the dictionary")
else:
        print(f"Key {key_search} is not in the dictionary")
