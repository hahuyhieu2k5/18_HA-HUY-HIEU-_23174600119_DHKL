import json

python_obj = {
    "ten": "HÀ HUY HIẾU",
    "tuoi": 19,
    "thanh_pho": "BẮC GIANG"
}

json_data = json.dumps(python_obj, indent=4, sort_keys=True)

print("Chuỗi JSON (sắp xếp theo khóa, thụt lề 4):\n", json_data)