f = open("Walden.txt",'rt')
lines = f.readlines()#将原文件内容按行读出并且保存在列表中
length = len(lines)
lines = [line.rstrip().ljust(length,)+'#'+str(index)+'\n'
         for index,line in enumerate(lines)]#  index?????
####for index,line in enumerate(open('Walden.txt','r')):
#####    count += 1
with open("makenew.txt",'a+')as f:#“a” 以“追加”模式打开
          #for line in lines:
           #    line_new = line.strip()#或使用  line_new = line.replace('\n', '') 替换删除
            #   line_new = (line_new + r'#' + 'count'+'\n') #在末尾+ # +换行符
             #  line_new = line_new.ljust(10)##这个我还是不太明白怎么做
            #如何再+行号呢？？？？？？？
         #print(line_new)
    f.writelines(lines)#将字符串序列写入文件
