import tkinter as tk

def submit_action():
    
    student_name = name_entry.get()
    student_id = id_entry.get()
    password = password_entry.get()

    print("Tên sinh viên:", student_name)
    print("ID sinh viên:", student_id)
    print("Mật khẩu:", password)

window = tk.Tk()
window.title("Thông tin sinh viên")
window.geometry("400x300")

# Nhãn và hộp nhập liệu cho tên sinh viên
name_label = tk.Label(window, text="Tên sinh viên:", font=("Arial", 12))
name_label.pack(pady=5)
name_entry = tk.Entry(window, font=("Arial", 12), width=30)
name_entry.pack(pady=5)

# Nhãn và hộp nhập liệu cho ID sinh viên
id_label = tk.Label(window, text="ID sinh viên:", font=("Arial", 12))
id_label.pack(pady=5)
id_entry = tk.Entry(window, font=("Arial", 12), width=30)
id_entry.pack(pady=5)

# Nhãn và hộp nhập liệu cho mật khẩu
password_label = tk.Label(window, text="Mật khẩu:", font=("Arial", 12))
password_label.pack(pady=5)
password_entry = tk.Entry(window, font=("Arial", 12), width=30, show="*")
password_entry.pack(pady=5)

# Nút gửi
submit_button = tk.Button(window, text="Gửi", font=("Arial", 12), command=submit_action)
submit_button.pack(pady=20)

# Vòng lặp chính để hiển thị giao diện
window.mainloop()

