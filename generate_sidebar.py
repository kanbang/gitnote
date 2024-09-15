'''
Descripttion: 
version: 0.x
Author: zhai
Date: 2024-09-15 20:34:51
LastEditors: zhai
LastEditTime: 2024-09-15 20:39:46
'''
import os

# 设置需要遍历的文件夹路径和生成的 _sidebar.md 路径
folder_path = '10x程序员工作法笔记'
sidebar_path = os.path.join(folder_path, '_sidebar_gen.md')

# 设置文档的基准路径（用于生成链接）
base_path = f"/{folder_path}/"

# 打开 _sidebar.md 文件以写入
with open(sidebar_path, 'w', encoding='utf-8') as sidebar_file:
    # 遍历文件夹中的所有文件
    for filename in sorted(os.listdir(folder_path)):
        # 获取文件扩展名，确保只处理特定类型的文件（如 markdown 文件）
        if filename.endswith('.md') and filename != '_sidebar.md':
            # 去掉文件扩展名
            file_title = os.path.splitext(filename)[0]
            
            # 替换空格为'-'，生成 URL 路径友好的标题
            link_title = file_title.replace(' ', '-')
            
            # 生成链接，格式为 - [标题](路径)
            sidebar_entry = f'- [{file_title}]({base_path}{link_title})\n'
            
            # 写入 _sidebar.md 文件
            sidebar_file.write(sidebar_entry)

print(f'_sidebar_gen.md 文件已成功生成于 {folder_path}。')
