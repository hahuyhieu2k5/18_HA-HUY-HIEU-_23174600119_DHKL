import math

class Diem:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Elip(Diem):
    def __init__(self, x, y, a, b):
        super().__init__(x, y)
        self.a = a  
        self.b = b  

    def tinh_dien_tich(self):
        return math.pi * self.a * self.b

class DuongTron(Elip):
    def __init__(self, x, y, r):
        super().__init__(x, y, r, r)

elip = Elip(2, 2, 7, 6)
print(f"Diện tích elip: {elip.tinh_dien_tich():.2f}")

duong_tron = DuongTron(3, 2, 7)
print(f"Diện tích đường tròn: {duong_tron.tinh_dien_tich():.2f}")