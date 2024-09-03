import xml.etree.ElementTree as ET
import os

# 假设classes是一个包含所有类别名称的列表
classes = ["airplane", "Building", "2", "3", "overpass", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18"]

def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

def convert_annotation(xml_path, output_path):
    in_file = open(xml_path, 'r')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    
    with open(output_path, 'w') as f:
        for obj in root.iter('object'):
            cls = obj.find('name').text
            if cls not in classes:
               continue
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
            bb = convert((w, h), b)
            f.write(str(classes.index(cls)) + " " + " ".join([str(a) for a in bb]) + "\n")
    in_file.close()

# 转换所有XML文件
xml_folder = 'D:\\last\\test\\1-Building\\xml_labels01' # 替换为您的XML文件所在的文件夹路径
output_folder = 'D:\\last\\test\\1-Building\\labels01' # 替换为您希望生成YOLO格式文件的文件夹路径
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for xml_file in os.listdir(xml_folder):
    if xml_file.endswith('.xml'):
        convert_annotation(os.path.join(xml_folder, xml_file), os.path.join(output_folder, os.path.splitext(xml_file)[0] + '.txt'))
        