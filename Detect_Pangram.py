"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.s

"""
"""
Proposed solution:

We can create a check list for all letters of the alphabet, when a letter is found we check in that check list 
and if a letter that is already check is passed, we skip and when all the check list is fully checked. return true else false. 
We also ignore numbers and punctions (special characters)

"""