#词频统计
        #噪音处理
def getText():
    txt = open("Walden.txt","r").read()#打开文件
    txt = txt.lower() #避免对词频统计的干扰，将大写变成小写
    for ch in '!?,./|\;:"-=_': #筛选文字中的标点符号
        txt = txt.replace(ch," ") #将特殊符号replace替换成空格
        return txt
WaldenTxt = getText()#读取文件
words = WaldenTxt.split()#分隔单词，让他们变成一个列表
counts = {}
for word in words:
    counts[word] = counts.get(word,0)+1
    #counts.get 用来从字典中获得键对应的值，如果这个键不在字典当中，给出默认值
    #counts.get(word, 0)用当前的一个单词作为键索引字典，如果在里面则返回次数，
    #如果不在里面则加到字典中，赋当前值为0.

items = list(counts.items())#将字典类型转化为列表类型便于操作。
items.sort(key=lambda x:x[1], reverse=True) #将第二维数据的值进行排序， reverse=True降序。
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word,count))#打印单词和对应出现的次数。