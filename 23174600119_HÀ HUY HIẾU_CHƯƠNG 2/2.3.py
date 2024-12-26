import xml.dom.minidom

doc = xml.dom.minidom.parse("sample.xml")

company = doc.documentElement

company_name = company.getElementsByTagName("name")[0].firstChild.data
print("Company Name:", company_name)

staffs = company.getElementsByTagName("staff")

for staff in staffs:
    staff_id = staff.getAttribute("id")
    staff_name = staff.getElementsByTagName("name")[0].firstChild.data
    staff_salary = staff.getElementsByTagName("salary")[0].firstChild.data
    print(f"Staff ID: {staff_id}, Name: {staff_name}, Salary: {staff_salary}")