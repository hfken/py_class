raw=input()

up=[chr(i) for i in range(65,100)]

if raw.islower():
    raw=raw.upper()

lo=1
for i in raw:
    if not i.isalpha():
        print(i,end='')
        lo+=1
        continue
    out=up.index(i)
    for j in range(lo):
        out+=1
        if out>25:
            out=0
    print(up[out],end='')
    lo+=1


