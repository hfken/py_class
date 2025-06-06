#try-except语句块
#try语句必须要有一个except或者finally块，否则报错
try:
    #包裹可能引发异常的代码
    pass

except ValueError:
    #用于捕获错误类型
    pass
except:
    pass
else:
    #如果正常运行，则执行else语句块内容
    pass
finally:
    #无论如何都会执行
    pass