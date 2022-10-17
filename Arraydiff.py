"""
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list
array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]

"""

"""
Explaination:
time complexity = O(n^2)
space complexity= ?

Rough solution

- We create a new array
- We make a complete search checking each element of list a with list b
- Append all element not in list b
"""
def array_diff(a, b):
	new_array = []
	for i in a:
		for z in b:
			if i != z:
				new_array.append(i)
	return new_array

