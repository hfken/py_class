s=input()
for i in s:
    if (i<'0' or i>'9') and i!='.':
        print('No')
        quit()
ip=s.split('.')

if len(ip)!=4:
    print('No')
    quit()

for n in ip:
    if int(n)<0 or int(n)>255:
        print('No')
        quit()

print('Yes')