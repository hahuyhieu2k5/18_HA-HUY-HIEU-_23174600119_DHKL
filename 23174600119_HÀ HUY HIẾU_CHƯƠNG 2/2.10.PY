import json
from datetime import datetime

giao_dich = [
    {"id": 1, "so_tien": 2000, "loai": "thu"},
    {"id": 2, "so_tien": 10001000, "loai": "chi"},
    {"id": 3, "so_tien": 5020, "loai": "thu"}
]

def ghi_giao_dich_vao_json(giao_dich):
    thoi_gian_hien_tai = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    ten_tap_tin = f"{thoi_gian_hien_tai}.json"
    
    with open(ten_tap_tin, 'w', encoding='utf-8') as file:
        json.dump(giao_dich, file, ensure_ascii=False, indent=4)
    print(f"Dữ liệu giao dịch đã được ghi vào tập tin {ten_tap_tin}")

chon = input("Bạn có muốn ghi giao dịch vào tập tin không? (1: Có, 0: Không): ")
if chon == "1":
    ghi_giao_dich_vao_json(giao_dich)
else:
    print("Không ghi dữ liệu vào tập tin.")