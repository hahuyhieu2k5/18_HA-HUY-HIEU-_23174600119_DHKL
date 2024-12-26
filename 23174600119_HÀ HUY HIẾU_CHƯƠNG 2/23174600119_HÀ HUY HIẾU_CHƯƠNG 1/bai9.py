class DaGiac:
    def __init__(self):
        self.canh = []

    def tinh_chu_vi(self):
        return sum(self.canh)

class HinhBinhHanh(DaGiac):
    def __init__(self, a, b):
        super().__init__()
        self.canh = [a, b, a, b]

    def tinh_dien_tich(self, h):
        return self.canh[0] * h

class HinhChuNhat(HinhBinhHanh):
    def __init__(self, a, b):
        super().__init__(a, b)

    def tinh_dien_tich(self):
        return self.canh[0] * self.canh[1]

class HinhVuong(HinhChuNhat):
    def __init__(self, a):
        super().__init__(a, a)

print("Kiểm tra lớp HinhBinhHanh:")
hbh1 = HinhBinhHanh(55, 66)
hbh2 = HinhBinhHanh(22, 66)
print(f"Hbh1 - Chu vi: {hbh1.tinh_chu_vi()}, Diện tích (chiều cao 5): {hbh1.tinh_dien_tich(5)}")
print(f"Hbh2 - Chu vi: {hbh2.tinh_chu_vi()}, Diện tích (chiều cao 7): {hbh2.tinh_dien_tich(7)}")

print("\nKiểm tra lớp HinhChuNhat:")
hcn1 = HinhChuNhat(66, 33)
hcn2 = HinhChuNhat(54,32 )
print(f"Hcn1 - Chu vi: {hcn1.tinh_chu_vi()}, Diện tích: {hcn1.tinh_dien_tich()}")
print(f"Hcn2 - Chu vi: {hcn2.tinh_chu_vi()}, Diện tích: {hcn2.tinh_dien_tich()}")

print("\nKiểm tra lớp HinhVuong:")
hv1 = HinhVuong(22)
hv2 = HinhVuong(33)
print(f"Hv1 - Chu vi: {hv1.tinh_chu_vi()}, Diện tích: {hv1.tinh_dien_tich()}")
print(f"Hv2 - Chu vi: {hv2.tinh_chu_vi()}, Diện tích: {hv2.tinh_dien_tich()}")