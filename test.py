def hash_code(s):
    mask = (1<<32)-1
    h=0
    for c in s:
        h = (h<<5 & mask) | (h>>27)
        print(h)
        h += ord(c)
        print(h)
    return h

print(hash_code('abc'))


print('.'.join(str(i) for i in range(5)))

