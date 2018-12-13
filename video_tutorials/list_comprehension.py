squares = [x * x for x in range(10)]

# As a "for" loop:

# 'Long' way
squares = []
for x in range(10):
    squares.append(x * x)

# With list comprehension
squares = [x * x for x in range(10)]

"""
Template

(values) = [ (expression) for (value) in (collection) ]

# Transforms into:

(values) = []
for (value) in (collection):
    (values).append ( (expression) )
"""

#continue from 5:34 filtering

