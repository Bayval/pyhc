class Vector:
    min_cord = 0
    max_cord = 50

    @classmethod
    def val(cls, arg):
        return cls.min_cord < arg < cls.max_cord

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.val(x) and self.val(y):
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x*x + y*y


v = Vector(1, 100)
res = Vector.get_coord(v)
print(res)
print(Vector.val(5))
print(Vector.norm2(5, 5))
