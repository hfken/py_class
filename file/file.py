with open(r'file/text.txt','r',encoding='utf-8') as f:
    f.seek(0,2)
    print(f.readline(),end='')
    
  

