# Create two sets of integers and find their difference, intersection, union and symmetric difference. Also find subset and superset from these two.
# Apply methods as well as operators for all operations.

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
set3 = {3,4,5}

print("Using Methods:")
print("Difference: ", set1.difference(set2))
print("Intersection: ", set1.intersection(set2))
print("Union: ", set1.union(set2))
print("Symmetric Difference: ", set1.symmetric_difference(set2))
print("Subset: ", set3.issubset(set2))
print("Superset: ", set1.issuperset(set3))


print("Using Operators:")
print("Difference: ", set1-set2)
print("Intersection: ", set1&set2)
print("Union: ", set1.union(set2))
print("Symmetric Difference: ", set1^set2)
print("Subset: ", set3 <= set2)
print("Superset: ", set1 >= set3)
