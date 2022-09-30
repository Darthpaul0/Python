numbers = [1, 2, 3]


class Point:
    # Constructor
    # We use self to refer to the object
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Class methods
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point(1, 2)
point1.x = 5
print(point1.x)
