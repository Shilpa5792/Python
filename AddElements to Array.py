import array as arr

# adding an element using insert()
print("adding an element using insert()")
a = arr.array('i', [1, 2, 3])

print("Array before insertion: ")
for i in (a):
    print(i, end=" ")
print()

a.insert(1,5)

print("Array after insertion: ")
for i in (a):
    print(i, end=" ")
print()
print()


# adding an element using append()
print("adding an element using append()")
b = arr.array('i', [1, 2, 3])

print("Array before insertion: ")
for i in (b):
    print(i, end=" ")
print()

b.append(5)

print("Array after insertion: ")
for i in (b):
    print(i, end=" ")
print()