f = open("Walden.txt",'rt')
lines = f.readlines()#将原文件内容按行读出并且保存在列表中
length = len(max(lines,key=len))
lines = [line.rstrip().ljust(length,)+'#'+str(index)+'\n'# rstrip()剔除右边的空格，字符。 
         for index,line in enumerate(lines)]# enumerate 迭代器， index：行号  line：对应的内容
####for index,line in enumerate(open('Walden.txt','r')):
#####    count = 0 
with open("makenew.txt",'w')as f1:#“a” 以“追加”模式打开
          #for line in lines:
                  count+=1
           #    line_new = line.strip()#或使用  line_new = line.replace('\n', '') 替换删除
            #  line_new = line_new.ljust()
             #   line_new = (line_new + r'#' + count+'\n') #在末尾+ # +换行符
         
         
            #如何再+行号呢？？？？？？？
         #print(line_new)
    f.writelines(lines)#将字符串序列写入文件
close("Walden.txt")
