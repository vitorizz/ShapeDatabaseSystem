class Shape:
    id = 0

    def __init__(self):
        Shape.id += 1
        # self.instance_id will be a class specific variable, each class will have their own value
        self.instance_id = Shape.id
        # I think, check later, but I think self.id would just refer to shapes id counter there
        self.name = "Shape"

    def perimeter(self):
        return

    def area(self):
        return

    def pr(self):
        print("{}: {}, perimeter: {}, area: {}".format(
            self.instance_id, self.name, self.perimeter(), self.area()))


class Circle(Shape):

    def __init__(self, radius):
        super().__init__()
        self.name = "Circle"
        self.radius = int(radius)

    def perimeter(self):
        return (2 * 3.1415926 * self.radius)

    def area(self):
        return (3.1415926 * self.radius * self.radius)

    def pr(self):
        print("{}: {}, perimeter: {:.5f}, area: {:.5f}".format(
            self.instance_id, self.name, self.perimeter(), self.area()))


class Ellipse(Shape):

    def __init__(self, a, b):
        super().__init__()
        self.name = "Ellipse"
        if a > b:
            self.semiMajor = int(a)
            self.semiMinor = int(b)
        else:
            self.semiMajor = int(b)
            self.semiMinor = int(a)

    def area(self):
        return (4 * self.semiMajor * self.semiMinor)

    def eccentricity(self):
        return (self.semiMajor**2 - self.semiMinor**2)**0.5

    def pr(self):
        print("{}: {}, perimeter: {}, area: {}, linear eccentricity: {:.5f}".format(
            self.instance_id, self.name, self.perimeter(), self.area(), self.eccentricity()))


class Rhombus(Shape):
    def __init__(self, diagonal_1, diagonal_2):
        super().__init__()
        self.name = "Rhombus"
        self.diagonal_1 = int(diagonal_1)
        self.diagonal_2 = int(diagonal_2)

    def side(self):
        return ((self.diagonal_1**2 + self.diagonal_2**2)**0.5)/2

    def perimeter(self):
        return self.side() * 4

    def area(self):
        return (self.diagonal_1 * self.diagonal_2)/2

    def inradius(self):
        return (self.diagonal_1 * self.diagonal_2) / \
            (((self.diagonal_1**2 + self.diagonal_2**2)**0.5)*2)

    def pr(self):
        print("{}: {}, perimeter: {:.5f}, area: {}, in-radius: {:.5f}".format(
            self.instance_id, self.name, self.perimeter(), self.area(), self.inradius()))
