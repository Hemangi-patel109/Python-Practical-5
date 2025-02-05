# Write a function called find_dups that takes a list of integers as its input argument and returns a set of those integers that occur two or more timesin the list.

def find_dups(int_list):
    counts = {}
    dups = set()
    for num in int_list:
        if num in counts:
            counts[num] += 1
            if counts[num] == 2:
                dups.add(num)
        else:
            counts[num] = 1  
    return dups

list1 = [1, 2, 3, 4, 2, 4, 6, 3]
dups1 = find_dups(list1)
print(f"Duplicates in {list1}: \n {dups1}")