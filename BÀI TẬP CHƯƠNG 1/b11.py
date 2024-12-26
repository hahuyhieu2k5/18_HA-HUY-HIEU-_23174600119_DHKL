import math

class TamGiac:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def tinh_chu_vi(self):
        return self.a + self.b + self.c

    def tinh_dien_tich(self):
        p = self.tinh_chu_vi() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

class TamGiacVuong(TamGiac):
    def __init__(self, a, b):
        c = math.sqrt(a**2 + b**2)
        super().__init__(a, b, c)

class TamGiacCan(TamGiac):
    def __init__(self, a, b):
        super().__init__(a, b, b)

class TamGiacDeu(TamGiacCan):
    def __init__(self, a):
        super().__init__(a, a)

print("Kiểm tra lớp TamGiac:")
tg1 = TamGiac(1, 2, 3)
tg2 = TamGiac(2, 3, 4)
print(f"Tam giác 1 - Chu vi: {tg1.tinh_chu_vi():.2f}, Diện tích: {tg1.tinh_dien_tich():.2f}")
print(f"Tam giác 2 - Chu vi: {tg2.tinh_chu_vi():.2f}, Diện tích: {tg2.tinh_dien_tich():.2f}")

print("\nKiểm tra lớp TamGiacVuong:")
tgv1 = TamGiacVuong(5, 6)
tgv2 = TamGiacVuong(7, 13)
print(f"Tam giác vuông 1 - Chu vi: {tgv1.tinh_chu_vi():.2f}, Diện tích: {tgv1.tinh_dien_tich():.2f}")
print(f"Tam giác vuông 2 - Chu vi: {tgv2.tinh_chu_vi():.2f}, Diện tích: {tgv2.tinh_dien_tich():.2f}")

print("\nKiểm tra lớp TamGiacCan:")
tgc1 = TamGiacCan(4, 5)
tgc2 = TamGiacCan(6, 7)
print(f"Tam giác cân 1 - Chu vi: {tgc1.tinh_chu_vi():.2f}, Diện tích: {tgc1.tinh_dien_tich():.2f}")
print(f"Tam giác cân 2 - Chu vi: {tgc2.tinh_chu_vi():.2f}, Diện tích: {tgc2.tinh_dien_tich():.2f}")

print("\nKiểm tra lớp TamGiacDeu:")
tgd1 = TamGiacDeu(5)
tgd2 = TamGiacDeu(6)
print(f"Tam giác đều 1 - Chu vi: {tgd1.tinh_chu_vi():.2f}, Diện tích: {tgd1.tinh_dien_tich():.2f}")
print(f"Tam giác đều 2 - Chu vi: {tgd2.tinh_chu_vi():.2f}, Diện tích: {tgd2.tinh_dien_tich():.2f}")