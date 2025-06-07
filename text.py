dict1 = {1: '周一',2: '周二', 3: '周三',4: '周四',5: '周五',6: '周六'}
for i in range(1,5):
    for j in range(i+1,5):
        print('{}考X'.format(dict1[i]),end=' ')
        print('{}考Y'.format(dict1[j]),end=' ')
        print('{}考Z'.format(dict1[5]))
for i in range(1,6):
    for j in range(i+1,6):
        print('{}考X'.format(dict1[i]),end=' ')
        print('{}考Y'.format(dict1[j]),end=' ')
        print('{}考Z'.format(dict1[6]))