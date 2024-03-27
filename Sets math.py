set1 = {1,2,3,4}
set2 = {3,4,5,6,7}

set2.add(8);

union_result = set1.union(set2)
print(union_result)

intersect = set1.intersection(set2)
print(intersect)

difference_result = set1.difference(set2)
print(difference_result)

symmetric_different = set1.symmetric_difference(set2)
print(symmetric_different)

is_subset = set1.issubset(set2)
print("Is set1 subset of set?" ,  is_subset)

is_super = set2.issuperset(set2)
print("Is set2 super set of set 2?", is_super)
print('Set 1 has: ' , str(len(set1)) + " elements")

