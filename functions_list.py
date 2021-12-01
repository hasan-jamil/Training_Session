x = [1, 2, 3, 1 , 1, True, 3.4, "Hello"]

x.pop()
print(x)

c = x.count(1)
print(c)

i = x.index(1)
print(i)

x.remove(1)
print(x)

list_contains_5 = 5 in x
f = x.count(5) > 0
print(list_contains_5)
print(f)

print(x[-1])



