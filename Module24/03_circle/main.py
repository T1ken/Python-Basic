from math import pi


class Circle:
    def __int__(self, x, y, r, k):
        self.x = x
        self.y = y
        self.r = r
        self.s = None
        self.k = k

    def search_s(self):
        return pi * (self.r ** 2)

    def search_p(self):
        return 2 * pi * self.r

    def multiplication(self):
        return self.r * self.k

    def is_intersect(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.r + other.r) ** 2
