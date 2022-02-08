#Using sort() method

list = [10, 20, 4, 45, 99, 67, 1029, 17]

list.sort()

print("2nd Largest element is:", list[-2])
print("2nd smallest element is:", list[1])


print()
#Providing user inputs

list = []

num = int(input("Enter number of elements in list: "))
print("Enter the elements")
for i in range(0, num):
    element = int(input(""))
    list.append(element)

print("2nd Largest element is:", sorted(list)[-2])
print("2nd smallest element is:", sorted(list)[1])
