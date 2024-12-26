from xml.dom.minidom import parse

file_path = 'sample.xml'
doc = parse(file_path)

names = doc.getElementsByTagName("name")
for name in names:
    print(name.firstChild.data)