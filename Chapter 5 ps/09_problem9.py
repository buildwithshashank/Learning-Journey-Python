s = {8, 7, 12, "Harry", [1,2]} 

#No—you cannot directly change the values inside a list that is stored in a set.

#Here’s why:

#A set in Python requires its elements to be immutable (hashable).
#A list is mutable, so it cannot be an element of a set at all.