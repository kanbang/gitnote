import os

# 指定要处理的文件夹路径
folder_path = '10x程序员工作法笔记'

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    # 如果文件名中包含空格
    if ' ' in filename:
        # 构造旧文件的完整路径
        old_file = os.path.join(folder_path, filename)
        
        # 去掉文件名中的空格（可以用replace替换成下划线，或直接去掉）
        new_filename = filename.replace(' ', '')
        
        # 构造新文件的完整路径
        new_file = os.path.join(folder_path, new_filename)
        
        # 重命名文件
        os.rename(old_file, new_file)
        print(f'Renamed: {filename} -> {new_filename}')
