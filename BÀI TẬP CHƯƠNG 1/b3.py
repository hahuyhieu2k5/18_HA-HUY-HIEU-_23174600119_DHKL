class PS:
    def __init__(self):
        self.tu_so = 0
        self.mau_so = 1

    def kiem_tra_hop_le(self):
        return self.mau_so != 0

    def nhap_phan_so(self):
        self.tu_so = int(input("Nhập tử số: "))
        self.mau_so = int(input("Nhập mẫu số: "))
        while not self.kiem_tra_hop_le():
            print("Mẫu số không hợp lệ. Vui lòng nhập lại.")
            self.mau_so = int(input("Nhập mẫu số: "))

    def hien_thi(self):
        print(f"{self.tu_so}/{self.mau_so}")

ps = PS()
ps.nhap_phan_so()
ps.hien_thi()