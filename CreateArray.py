import array as arr

a = arr.array('i', [1, 2, 3]) # i=unsigned integer

print("The created array is:", end=" ")
for i in range (0, 3):
    print(a[i], end=" ")
print()

b = arr.array('d', [5.5, 3.6, 9, 9.12])# d=double i.e., holds float type

print("Newly created array is:", end=" ")
for i in range (0, 4):
    print(b[i], end=" ")
print()
