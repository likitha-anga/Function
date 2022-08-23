# def function(a):
#     i=0
#     c=[]
#     while i<len(list):
#         d=list[i]
#         list.remove(d)
#         if a in list:
#             b=d,d
#             c.append(b)
#         i+=1
#     print(len(d))
# function([2,13,2,43,54,32,54,56,5,434,3,54,3,32,1])



list=[10,20,10,30,50,20,30,10,10,50]
i=0
c=[]
while i<len(list):
    a=list[i]
    list.remove(a)
    if a in list:
        b=a,a
        c.append(b)
    i=i+1
print(len(c))


