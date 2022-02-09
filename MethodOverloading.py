# Using default argument

class Calculate():
    print("\nUsing default argument\n")
    def add(self, a, b, c=0):
        if c > 0:
            print("a+b+c {}".format(a+b+c))
        else:
            print("a+b {}".format(a+b))

c1 = Calculate()

c1.add(1, 2, 3)
c1.add(1, 2)

# Using variable length argument

class Calculate1():
    print("\nUsing variable length argument\n")
    def add(self, *args):
        result = 0
        for param in args:
            result += param
        print("Result: {}".format(result))

c2 = Calculate1()

c2.add(10, 20, 30)
c2.add(10, 30)
c2.add(90, 45, 67, 43, 223)
