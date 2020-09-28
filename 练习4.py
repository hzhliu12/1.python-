#练习4:自定义求序列偶数个数的函数
def find_double(x): #定义一个函数
    list=0
    for i in x:
        if i%2==0:
            list+=1
    return list
tst= find_double([1,2,3,4,5,6,7,8,10])
print(tst)

