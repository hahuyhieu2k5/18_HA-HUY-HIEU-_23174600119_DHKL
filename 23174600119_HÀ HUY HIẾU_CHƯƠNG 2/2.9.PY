import json

data_json = '''
{
    "ten_cong_ty": "Công ty TNHH HIẾU BIN",
    "dia_chi": "XYZ TAM TRINH – Hà Nội",
    "don_vi": [
        {"ten_don_vi": "Đơn vị A1", "so_nhan_vien": 25},
        {"ten_don_vi": "Đơn vị A2", "so_nhan_vien": 35},
        {"ten_don_vi": "Đơn vị A3", "so_nhan_vien": 40},
        {"ten_don_vi": "Đơn vị A4", "so_nhan_vien": 35},
        {"ten_don_vi": "Đơn vị A5", "so_nhan_vien": 50}
    ]
}
'''

data = json.loads(data_json)

tong_so_nhan_vien = sum(dv["so_nhan_vien"] for dv in data["don_vi"])

print("Tên công ty:", data["ten_cong_ty"])
print("Địa chỉ:", data["dia_chi"])
print("-----Thống kê nhân viên theo đơn vị:-----")

for i, don_vi in enumerate(data["don_vi"], start=1):
    ten_don_vi = don_vi["ten_don_vi"]
    so_nhan_vien = don_vi["so_nhan_vien"]
    ty_le = (so_nhan_vien / tong_so_nhan_vien) * 100
    
    print(f"{i}/ Tên đơn vị: {ten_don_vi}")
    print(f"   - Số nhân viên: {so_nhan_vien}")
    print(f"   - Tỷ lệ: {ty_le:.2f}%")
