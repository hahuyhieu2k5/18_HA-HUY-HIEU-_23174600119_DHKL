import csv
import numpy as np

import csv
# Đọc dữ liệu fle csv
filename = "23174600119_HÀ HUY HIẾU_BÀI LAP/LAB2/Data/diem_hoc_phan.csv"
scores_list = []
with open(filename, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Bỏ qua header
    for row in reader:
        scores_list.append(float(row[0]))  # Giả định cột điểm nằm ở cột đầu tiên

    # Chuyển đổi sang mảng NumPy
scores_array = np.array(scores_list)

    # Tính toán các thống kê
average_score = np.mean(scores_array)
max_score = np.max(scores_array)
min_score = np.min(scores_array)
std_dev = np.std(scores_array)

    # Hiển thị kết quả
print(f"Điểm trung bình: {average_score:.2f}")
print(f"Điểm cao nhất: {max_score}")
print(f"Điểm thấp nhất: {min_score}")
print(f"Độ lệch chuẩn: {std_dev:.2f}")