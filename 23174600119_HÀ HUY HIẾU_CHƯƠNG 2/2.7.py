import json

python_obj = {
    "ten": "hà huy hiếu",
    "tuoi": 19,
    "thanh_pho": "Bắc giang"
}

json_data = json.dumps(python_obj)

print("Chuỗi JSON:", json_data)