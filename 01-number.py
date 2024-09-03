import os
import shutil

# 指定文件夹路径
folder_path = 'D:\\last\\train\\18-Vehicle\\labels'

# 获取文件夹内所有.jpg文件的列表
file_list = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

# 对文件列表进行排序，确保编号顺序正确
file_list.sort()

# 初始化编号
number = 36000

# 遍历文件列表并重命名文件
for file_name in file_list:
    # 构造新的文件名
    new_file_name = f"{number:05d}.txt"
    
    # 原始文件的完整路径
    old_file_path = os.path.join(folder_path, file_name)
    # 新文件的完整路径
    new_file_path = os.path.join(folder_path, new_file_name)
    
    # 使用shutil模块重命名文件
    shutil.move(old_file_path, new_file_path)
    
    # 打印重命名操作
    print(f"Renamed {file_name} to {new_file_name}")
    
    # 增加编号
    number += 1

print("All .jpg files have been successfully numbered.")