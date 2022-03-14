class TamGiacVuong:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c
    
    def isTamGiacVuong(self) -> bool:
        return self.a * 2 + self.b * 2 == self.c * 2 or self.a * 2 + self.c * 2 == self.b * 2 or self.b * 2 + self.c * 2 == self.a ** 2
        
    def area(self) -> int:
        s = (self.a + self.b + self.c) / 2
        return int((s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5)

    def parameter(self) -> int:
        return self.a + self.b + self.c

a, b, c = [int(x) for x in input().split()]
tamGiac = TamGiacVuong(a, b, c)
if tamGiac.isTamGiacVuong():
    print(tamGiac.parameter(), tamGiac.area())
else:
    print("INVALID")