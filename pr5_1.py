# Create a set of integers as follows:
# 1 initialize the set directly
# 2 initialize empty set and then add values
# 3 from a list
# 4 from another set
# 5 using range
# 6 update an existing set using another set
# 7 print the elements of set iteratively
# 8 check the functionality of remove and discard

set1 = {1,2,3,4,5}
print("Set created directly: ",set1)
set2 = set()
set2.add(71)
set2.add(70)
print("Set created by adding values: ",set2)
set3 = set(list([1,2,3,4,5]))
print("Set created from a list: ",set3)
set4 = set(set3)
print("Set created from another set: ",set4)
set5 = set(range(10,16))
print("Set created using range: ",set5)
set2.update(set5)
print("Set updated using another set: ",set2)
print("Elements of set1: ")
for i in set1:
    print(i)
set6 = {271,22,108,1415}
set6.remove(22)
print("Set after removing 22: ",set6)
set6.discard(1415)
print("Set after discarding 1415: ",set6)