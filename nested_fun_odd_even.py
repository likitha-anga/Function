# def fun():
#     i=0
#     a=[]
#     while i<10:
#         a.append(i)
#         i+=1
#     return a
# def fun1():
#     b=fun()
#     j=0
#     c=[]
#     d=[]
#     while j<len(b): 
#         if b[j]%2==0:
#             c.append(b[j])
#         else:
#             d.append(b[j])
#         j+=1
#     return c,d
# print(fun1())



    
# def fun():
#     i=1
#     a=[]
#     while i <=10:
#         a.append(i)
#         i=i+1
#     return a
# def fun1():
#     b=fun()
#     j=0
#     c=[]
#     while j<len(b):
#         c.append(b[:3])
#         c.append(b[-1:-4:-1])
#         j=j+10
#     print(c)
# fun1()


# def fun(a):
#     i=0
#     b=[]
#     c=[]
#     while i<len(a):
#         if a[i]>0:
#             b.append(a[i])
#         else:
#             c.append(a[i])
#         i=i+1
#     return b,c
        
# print(fun([1,3,-4,-9,4,12,21,-60]))

# def multi(a):
#     def mul(b):
#         return a*b
#     return mul
# y=multi(10)(30)
# print(y)


# list=[4,3,2,8]
# o/p=[43,42,48,32,38,28]

# list=[4,3,2,8]
# i=0
# a=[]
# while i<len(list):
#     j=0
#     while j<len(list)-1:
#         if 
#         a.append(str(list[i])+str(list[j+1]))
#         j+=1
#     i+=1
# print(a)



l=[4,3,2,8]
a=[]
i=0
while i<len(l):
    j=i
    while j<len(l)-1:
        c=str(l[i])+str(l[j+1])
        a.append(c)
        j=j+1
    i+=1
print(a)


def function(l):
    a=[]
    i=0
    while i<len(l):
        j=i
        while j<len(l)-1:
            c=str(l[i])+str(l[j+1])
            a.append(c)
            j=j+1
        i+=1
    print(a)
l=[4,3,2,8]
function(l)










