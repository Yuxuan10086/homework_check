import os
import csv

names = {}
with open('name.csv') as csv_file:
    names_csv = csv.reader(csv_file, delimiter = ',')
    for data in names_csv:  # 将名单存储至names字典,key为姓名,value为状态,1表示已交,0表示未交
        names[data[0]] = data[1]
    csv_file.close()

path = os.listdir(os.getcwd() + '\\source')
for p in path:
    if 'html' in p:
        os.rename('source\\' + p, 'source\\' + p.strip('html') + 'txt') # HTML文件重命名为txt文件
        with open('source\\' + p.strip('html') + 'txt', 'r', encoding = 'UTF-8') as f:
            source = f.read()
            f.close()
        for name, val in names.items():
            if name in source:
                names[name] = 1 # 遍历字典,判断姓名是否在源代码里
'''
改进空间:直接检索过于耗时,可以使用正则表达式
'''
print(names)

# no_list = []
# for name, val in names.items():
#     if not int(val):
#         no_list.append(name)
# print(no_list)
with open('res.txt', 'w', encoding = 'UTF-8') as f:
    for name, val in names.items():
        if not int(val):
            f.write(name) # 输出值为0的键
            f.write('\n')
    f.close()

try:
    import shutil
    shutil.rmtree(path = 'source')
except:
    pass