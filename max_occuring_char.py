from collections import Counter
s="hello"
common=Counter(s).most_common(1)[0]
print(common)
