import json
json_data = '{"ten": "HÀ HUY HIẾU", "tuoi": 19, "thanh_pho": "Bắc gianggiang"}'
python_obj = json.loads(json_data)
print("Đối tượng Python:", python_obj)