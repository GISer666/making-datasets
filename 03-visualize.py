import cv2
import numpy as np

def draw_yolo_boxes(image_path, label_path, class_names):
    # 读取图像
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    # 读取YOLO标签文件
    with open(label_path, 'r') as f:
        lines = f.readlines()

    # 在图像上绘制边界框
    for line in lines:
        parts = line.strip().split()
        class_id, x_center, y_center, box_width, box_height = map(float, parts)
        x_center, y_center, box_width, box_height = int(x_center * width), int(y_center * height), int(box_width * width), int(box_height * height)
        xmin = int(x_center - box_width / 2)
        ymin = int(y_center - box_height / 2)
        xmax = int(x_center + box_width / 2)
        ymax = int(y_center + box_height / 2)

        # 绘制边界框
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (255, 0, 0), 2)

        # 在图像上添加类别标签
        label = class_names[int(class_id)]
        cv2.putText(image, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # 显示图像
    cv2.imshow('Image with YOLO Boxes', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 使用示例
image_path = 'D:\\last\\test\\1-Building\\images\\1000.jpg'
label_path = 'D:\\last\\test\\1-Building\\labels\\1000.txt'
class_names = ["Airplane", "Building", "2", "3", "Bridge", "5", "6", "7", "8", "9", "10", "11", "12", "Ship", "14", "15", "16", "17", "Vehicle"]  # 替换为YOLO数据集的实际类别

draw_yolo_boxes(image_path, label_path, class_names)