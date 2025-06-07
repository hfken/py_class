import jieba
with open('jieba/text.txt','r',encoding='utf-8') as f:
    content=f.read()
    words=jieba.cut(content)#分词，cut（）函数返回的是一个迭代器，可以节省内存和资源
    #或者直接用lcut（）函数，返回一个列表，即所有分词结果，占用的内存更大点
    words_fre={}
    for i in words:
        if len(i)<2:
            continue
        if i in words_fre:
            words_fre[i]+=1
        else:
            words_fre[i]=1
    sor_word=sorted(words_fre.items(),key=lambda x:x[1],reverse=True)
    print(sor_word[:5])

