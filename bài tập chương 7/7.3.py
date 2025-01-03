import tkinter as tk

window = tk.Tk()

window.title("Thay đổi kiểu phông chữ nhãn")

window.geometry("500x350")  

label = tk.Label(window, 
                 text="Phông chữ tùy chỉnh", 
                 font=("Times New Roman", 18, "bold"))
label.pack(pady=20) 


window.mainloop()