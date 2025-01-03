import tkinter as tk

window = tk.Tk()

window.title("Cửa sổ Tkinter với Nhãn")

window.geometry("400x300") 


label = tk.Label(window, text="Chào mừng đến với nhà  HÀ HUY HIẾU", font=("Arial", 14))
label.pack(pady=20)  

window.mainloop()