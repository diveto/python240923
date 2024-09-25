import openpyxl
import random

# 엑셀 파일 생성
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Product Sales Data"

# 헤더 추가
ws.append(["Product ID", "Product Name", "Quantity", "Price"])

# 샘플 제품명 목록
product_names = ["Laptop", "Smartphone", "Tablet", "Monitor", "Keyboard", "Mouse", "Headphones", "Printer", "Smartwatch", "Camera"]

# 데이터 생성 및 추가
for i in range(1, 101):
    product_id = f"P{i:03d}"
    product_name = random.choice(product_names)
    quantity = random.randint(1, 100)
    price = round(random.uniform(50, 1500), 2)
    ws.append([product_id, product_name, quantity, price])

# 엑셀 파일 저장
file_path = "products.xlsx"
wb.save(file_path)

file_path
