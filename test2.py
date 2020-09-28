#编写一个列表处理程序
##使用input（）函数接收一个列表，打印输出列表中所有不重复的元素
#list1=eval(input("请输入列表："))
#print(list1)
#print(list(set(list1)))
#str = input('以空格为间隔连续输入一个数组:')
#list1= [int(n) for n in str.split()]
#list2=[]
list1=eval(input("请输入一个列表："))
#list2=[int(n) for n in list1.split()]  #list.split()用于拆分list1中的字符串
list3=[]
for i in list1:
    if i not in list3:
        list3.append(i)
    print(list3)
