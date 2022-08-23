# def function(a):
#     i=0
#     while i<len(a):
#         if user==a[i][0]:
#             print(a[i])
#         i+=1
# user=input("enter the number:")
# function(["anga amara","anga govind","kolati srinu","kolati vara"])



list="likiHarshaInduAlluRahulKiran"
i=0
upper=0
lower=0
while i<len(list):
    if list[i].isupper():
        upper+=1
    else:
        lower+=1
    i+=1
print(upper)
print(lower)
