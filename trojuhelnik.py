import math 

rangeIndexStart = 1
rangeIndexEnd = 2

#rovnoramenny pravohuly trojuhelnik s N v c
for i in range(rangeIndexStart,rangeIndexEnd):
    c=i
    a=math.sqrt((pow((c/2),2))+(pow((c/2),2)))
    b=math.sqrt((pow((c/2),2))+(pow((c/2),2)))

#rovnoramenny pravohuly trojuhelnik s N v a a b
for i in range(rangeIndexStart,rangeIndexEnd):
    x=i
    y=i
    z=math.sqrt((pow(x,2))+(pow(y,2)))
    print(z)


