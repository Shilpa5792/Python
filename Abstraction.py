import abc

class Shapes(abc.ABC):
    @abc.abstractmethod
    def sides(self):
        pass

class Triangle(Shapes):

    def sides(self):
        print("Triangle have 3 sides")

class Quadrilateral(Shapes):

    def sides(self):
        print("Quadrilateral have 4 sides")

class Pentagon(Shapes):

    def sides(self):
        print("Pentagon have 5 sides")

class Hexagon(Shapes):

    def sides(self):
        print("Hexagon have 6 sides")

T = Triangle()
T.sides()

Q = Quadrilateral()
Q.sides()

P = Pentagon()
P.sides()

H = Hexagon()
H.sides()
