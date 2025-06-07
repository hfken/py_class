with open(r'file\text.txt','r+',encoding='utf-8') as f:
    f.writelines('nihao')
    f.write('nihao')
    f.write('3')
    f.seek(0)
    f.write('3')

