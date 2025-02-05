my_dict = {'a': 1, 'b': 2, 'c': 2, 'd': 4}
key_remove = 'b'
if key_remove in my_dict:
    del my_dict[key_remove]
    print(f"key {key_remove} is removed.")
else:
    print(f"key {key_remove} is not found.")
print("Updaed Dictionary: ",my_dict)
