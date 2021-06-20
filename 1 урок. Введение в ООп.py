class Point(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self._z = 0
        print(f'Я родился в (0, 0)')

    def distance(self, x, y):
        return ((self.x - x) ** 2 + (self.y - y) ** 2) ** 0,5

    def __del__(self):
        print(f'я умир в точке ({self.x}, {self.y})')

    def __str__(self):
        print(f'({self.x}, {self.y})')

    def __call__(self, x, y):
        return x * y

    @staticmethod
    def help():
        print('НА помосчь!')

def explode():
    print('БАБАБАБАБАББАБАББААААААХАААААААААХААААХХХХХХХХХХХХХХХХХХ')

Point.help()
aboba = Point()
Point.color = 'green'
Point.sus = 'amogus'
Point.boom = explode()
print(aboba.distance(3, 4))
print(aboba.x, aboba.y)
print(aboba._z)
del aboba