##练习1:求y=sin(x)从0到2*pi，与x轴围成的面积

import math
num = 10000 #正弦函数的份数
x = []
for i in range(0,num+1):
    x.append(2*math.pi/num*i)
y = []
for j in y:
    y.append(abs(math.sin(j)))
    print(2*math.pi*sum(y)/num)