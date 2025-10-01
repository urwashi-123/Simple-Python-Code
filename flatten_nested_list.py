from itertools import chain
nested=[[1,2],[3,4]]
print(nested)
print(list(chain.from_iterable(nested)))