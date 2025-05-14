import os
import datetime

# Thông tin dự án
project_name = input("Nhập tên dự án: ") or "My Project"
description = input("Nhập mô tả dự án: ") or "A simple project to demonstrate README generation."
author = input("Nhập tên tác giả: ") or "Your Name"

# Lấy danh sách file trong thư mục hiện tại
files = [f for f in os.listdir() if os.path.isfile(f) and f != "generate_readme.py" and f != "README.md"]

# Tạo nội dung README
readme_content = f"""# {project_name}

## Mô tả
{description}

## Tác giả
{author}

## Ngày tạo
{datetime.datetime.now().strftime('%Y-%m-%d')}

## Cài đặt
```bash
# Ví dụ lệnh cài đặt
pip install -r requirements.txt
```

## Cách sử dụng
```bash
python main.py
```

## Cấu trúc dự án
Danh sách các file trong dự án:
{chr(10).join([f'- {f}' for f in files])}

## Giấy phép
MIT License
"""

# Ghi nội dung vào file README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("File README.md đã được tạo thành công!")