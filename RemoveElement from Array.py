import array as arr

a = arr.array('i', [1, 2, 3, 4, 5, 6]) # i=unsigned integer

print("The created array is:", end=" ")
for i in (a):
    print(i, end=" ")
print()
print()


# removing an element using pop()
print("removing an element using pop()")
print("The popped element is: ", end=" ")
print(a.pop(2))

print("The array after popping is: ", end=" ")
for i in (a):
    print(i, end=" ")
print()
print()


# removing an element using remove()
print("removing an element using remove()")
a.remove(5)

print("The array after removing an element: ", end=" ")
for i in (a):
    print(i, end=" ")
print()
print()