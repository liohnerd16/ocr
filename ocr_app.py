import cv2
import pytesseract
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

# Đường dẫn tới Tesseract executable (cập nhật nếu cần)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class OCRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng dụng Nhận diện Ký tự")
        self.root.geometry("800x600")
        self.root.configure(bg='#2b2b2b')  # Nền dark mode

        # Biến lưu trữ ảnh
        self.image_path = None
        self.image_label = None

        # Tạo giao diện
        self.create_widgets()

    def create_widgets(self):
        # Nút chọn ảnh
        self.select_button = tk.Button(
            self.root, 
            text="Chọn Ảnh", 
            command=self.load_image,
            bg='#3c3f41',  # Màu nền nút
            fg='#ffffff',  # Màu chữ
            activebackground='#4b4b4b',
            activeforeground='#ffffff'
        )
        self.select_button.pack(pady=10)

        # Nút nhận diện văn bản
        self.recognize_button = tk.Button(
            self.root, 
            text="Nhận diện Văn bản", 
            command=self.recognize_text,
            bg='#3c3f41',
            fg='#ffffff',
            activebackground='#4b4b4b',
            activeforeground='#ffffff'
        )
        self.recognize_button.pack(pady=10)

        # Khung hiển thị ảnh
        self.image_frame = tk.Frame(self.root, bg='#2b2b2b')
        self.image_frame.pack(pady=10)

        # Khung hiển thị văn bản
        self.text_label = tk.Label(
            self.root, 
            text="Văn bản nhận diện:", 
            bg='#2b2b2b', 
            fg='#ffffff'
        )
        self.text_label.pack(pady=5)

        self.text_area = tk.Text(
            self.root, 
            height=10, 
            width=80,
            bg='#3c3f41',
            fg='#ffffff',
            insertbackground='#ffffff',  # Màu con trỏ
            borderwidth=1,
            relief='solid'
        )
        self.text_area.pack(pady=5)

    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")])
        if self.image_path:
            # Xóa ảnh cũ nếu có
            if self.image_label:
                self.image_label.destroy()

            # Hiển thị ảnh
            img = Image.open(self.image_path)
            img = img.resize((400, 300), Image.Resampling.LANCZOS)  # Thay đổi kích thước ảnh
            img_tk = ImageTk.PhotoImage(img)
            self.image_label = tk.Label(self.image_frame, image=img_tk, bg='#2b2b2b')
            self.image_label.image = img_tk  # Giữ tham chiếu ảnh
            self.image_label.pack()

    def recognize_text(self):
        if not self.image_path:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một ảnh trước!")
            return

        try:
            # Đọc ảnh bằng OpenCV
            img = cv2.imread(self.image_path)
            if img is None:
                raise Exception("Không thể đọc ảnh!")

            # Chuyển sang ảnh xám
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Tăng độ tương phản
            gray = cv2.convertScaleAbs(gray, alpha=1.1, beta=0)

            # Nhận diện văn bản
            text = pytesseract.image_to_string(gray, lang='eng')  # Sử dụng 'eng' hoặc ngôn ngữ phù hợp
            self.text_area.delete(1.0, tk.END)  # Xóa nội dung cũ
            self.text_area.insert(tk.END, text.strip() or "Không nhận diện được văn bản.")

        except Exception as e:
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {str(e)}")

def main():
    root = tk.Tk()
    app = OCRApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()