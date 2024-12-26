class HinhChuNhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def tinh_chu_vi(self):
        return 2 * (self.dai + self.rong)

    def tinh_dien_tich(self):
        return self.dai * self.rong

    def in_thong_tin(self):
        print("Hình chữ nhật có:")
        print("Chiều dài: {}".format(self.dai))
        print("Chiều rộng: {}".format(self.rong))
        print("Chu vi: {}".format(self.tinh_chu_vi()))
        print("Diện tích: {}".format(self.tinh_dien_tich()))

dai = float(input("Nhập chiều dài: "))
rong = float(input("Nhập chiều rộng: "))
hcn = HinhChuNhat(dai, rong)
hcn.in_thong_tin()