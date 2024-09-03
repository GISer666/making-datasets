from PIL import Image
import os

def convert_png_to_jpg(source_folder, target_folder):
    # 确保目标文件夹存在，如果不存在则创建
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # 遍历源文件夹中的所有文件
    for filename in os.listdir(source_folder):
        if filename.lower().endswith('.png'):  # 检查文件是否为PNG格式
            # 构建完整文件路径
            source_path = os.path.join(source_folder, filename)
            # 构建目标文件路径，将.png替换为.jpg
            target_path = os.path.join(target_folder, filename.replace('.png', '.jpg'))

            # 打开图像文件
            with Image.open(source_path) as img:
                # 转换图像格式并保存为JPG
                img.convert('RGB').save(target_path, 'JPEG')

# 使用函数，指定源文件夹和目标文件夹
source_folder = 'D:\\second\\111'
target_folder = 'D:\\second\\222'

convert_png_to_jpg(source_folder, target_folder)