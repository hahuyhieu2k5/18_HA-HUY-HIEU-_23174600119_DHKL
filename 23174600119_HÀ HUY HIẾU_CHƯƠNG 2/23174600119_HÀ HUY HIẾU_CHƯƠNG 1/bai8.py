class Date:
    def __init__(self, day=27, month=10, year=2005):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year}"

class Employee:
    def __init__(self, name, birth_date, join_date):
        self.name = name
        self.birth_date = birth_date
        self.join_date = join_date

    def display(self):
        return f"Tên: {self.name}, Ngày sinh: {self.birth_date.display()}, Ngày vào công ty: {self.join_date.display()}"

class QuanLyNhanVien:
    def __init__(self):
        self.employees = []

    def them_nhan_vien(self, employee):
        self.employees.append(employee)

    def hien_thi_tat_ca(self):
        for i, emp in enumerate(self.employees, 1):
            print(f"Nhân viên {i}: {emp.display()}")

qlnv = QuanLyNhanVien()

qlnv.them_nhan_vien(Employee("HÀ HUY HH", Date(), Date(2, 11, 2024)))
qlnv.them_nhan_vien(Employee("HÀ THỊ KK", Date(1, 2, 2005), Date(15, 7, 2024)))

print("Danh sách tất cả nhân viên:")
qlnv.hien_thi_tat_ca()