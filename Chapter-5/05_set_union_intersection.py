s1 = {1, 2, 3, 4, 5}
s2 = {1, 5, 6, 7, 8}
print(s1.union(s2))
print(s1.intersection(s2))
print({1,5}.issubset(s2))
print(s1.issuperset({5}))
print(s1.isdisjoint(s2))
print(s1.difference(s2))