import jieba
with open('jieba/text.txt','r',encoding='utf-8') as f:
    content=f.read()
    words=jieba.lcut(content)#分词
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

