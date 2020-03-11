import os
path = os.listdir(os.getcwd() + '\\source')
for p in path:
    if 'txt' in p:
        os.rename('source\\' + p, 'source\\' + p.strip('txt') + 'html') # HTML文件重命名为txt文件
