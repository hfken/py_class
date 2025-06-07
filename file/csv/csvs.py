import csv
#读
with open('file/csv/data.csv','r',encoding='utf-8') as file:
    csv_read=csv.reader(file)#用于返回一个csv对象
    print(list(csv_read))#转换成list输出
with open('file/csv/data.csv','a',newline='') as f:
    csv_write=csv.writer(f)
    csv_write.writerow(['liming','19','77'])#写入一行
    csv_write.writerows([['liming','19','77'],['xiaomei','18','78']])#写入多行