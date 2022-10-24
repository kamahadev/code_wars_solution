
"""
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.

Don't forget the space after the closing parentheses!

"""
"""
input a list of number
return a string formated
"""
"""
Test solution

step 1: convert list of integer to string
step 2: insert parantheses at 0 position and 4 position
setp 3: insert a space at position 5
step 4: insert dash at position 10
"""

number  = [1,2,3,4,5,6,7,8,9,0]
string_num = [str(x) for x in number]
string_num.insert(0, "(")
string_num.insert(4, ")")
string_num.insert(5, " ")
string_num.insert(10, "-")
joined = ''.join(str(e) for e in string_num)

print(joined)
