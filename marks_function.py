def marks(list):
    i=0
    s=[]
    b=0
    while i<len(list):
        a=sum(list[i])
        b=b+a
        s.append([a])
        i+=1
    print("sum of list:" ,b)
list=[[78,76,94,86,88],[91,71,98,65,76],[95,45,48,52,49]]
marks(list)
