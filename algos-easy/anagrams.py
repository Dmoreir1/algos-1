# Anagrams

# Write a function, anagrams, that takes in two strings as arguments. 
# The function should return a boolean indicating whether or not the strings are anagrams. 
# Anagrams are strings that contain the same characters, but in any order.

def anagrams(s1, s2):
  s1 = sorted(s1)
  s2 = sorted(s2)
  if s1 == s2:
    print("True")
  else:
    print("False")






# # TEST CASES
anagrams('restful', 'fluster') # -> True
anagrams('cats', 'tocs') # -> False
anagrams('monkeyswrite', 'newyorktimes') # -> True
anagrams('paper', 'reapa') # -> False
# anagrams('elbow', 'below') # -> True
# anagrams('tax', 'taxi') # -> False
# anagrams('taxi', 'tax') # -> False
# anagrams('night', 'thing') # -> True
# anagrams('po', 'popp') # -> False
# anagrams('pp', 'oo') # -> False

#
# if len(s1)!= len(s2):
#   return false
#
# count = {}
# for char in s1
#   count[char] = 1
# else: count[char] += 1
#
# for char in s2
#   if char char not in count:
#     return False
#   else: count[char] -= 1
#   if count[char] < 0
#         return False
# return True