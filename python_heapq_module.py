import heapq as h
list1 = [1, 4, 7, 9, 0, -4, 20, 6, 2]
list2 = [(1, 'gh'), (3, 'uy'), (0, 'gugb'), (9, 'gtf'), (-6, 'shswa')]
list3 = []

# Functions of heapq module.

# If you start adding in empty list it will sort as well but if you add in list having some ekement in the it then it simply add in the last of the list.To sort this you have to call heapyfy.

for i in list1:
    h.heappush(list3, i)
h.heappush(list3, 8)
print(list3)
h.heapify(list1)
h.heappush(list2, (5, "nag"))


print(h.heappop(list1))
print(h.heappop(list1))
print(h.heappop(list3))
print(h.heappop(list3))


h.heappushpop(list3, 87)
print(list3)


print(h.nlargest(3, list3))
print(h.nsmallest(3, list3))


#some more methods;

# h.heapreplace
# h.merge
# h._heapify_max













