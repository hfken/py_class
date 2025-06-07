with open(r'file/text.txt','w',encoding='utf-8',newline='\n') as fw,\
open(r'file/text.txt','r',encoding='utf-8',newline='\n') as fr:
    fw.writelines('\n'.join(['hello','hi']))
    fw.seek(0)
    print(repr(fr.readline()))
    
  

