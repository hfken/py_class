#文件
with open(r'text.txt','rt',encoding='utf-8') as f:
    print(repr(f.read()))#repr读取原始文本 即abcd\nvcfd
    f.seek(0)#文件读取头归零
    print(f.readlines())#以行形式读取，返回一个列表
    f.seek(0)
    a=f.readlines(0)#读取第一行
    print(a)
    #seek函数：seek([移动的字节数，+为右，-为左])
    #在文本时，
'''
打开模式
前缀 r读取（默认值） w写入，首先清空文件 x独占创建文件 若文件存在 则失败； a追加模式，打开写入文件，如果文件存在则追加
后缀 t文本模式 b二进制模式 +打开磁盘文件进行更新 如果文件不存在就会创建文件
'''



	
