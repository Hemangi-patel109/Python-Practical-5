def check_empty_dict(list1):
    return all(len(d) == 0 for d in list1)
dict_list = [{},{},{}]
result = check_empty_dict(dict_list)
if result:
    print("All dictionaries in the list are empty")
else:
    print("At least one dictionary in the list is not empty")