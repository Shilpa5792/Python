#Using sort() method

list = [10, 20, 4, 45, 99, 67, 1029, 17]

list.sort()

print("Largest element is:", list[-1])

#Using max() method

list = [18, 202, 4, 45, 9, 26]

print("Largest element is:", max(list))

#Using user inputs with max()

list = []

num = int(input("Enter number of elements in list: "))
print("Enter the elements")
for i in range(0, num):
    element = int(input(""))
    list.append(element)

print("Largest element is:", max(list))
