def my_function(speed):
    if speed<=70:
        print("70")
    elif 70<=speed:
        a=((speed-70)//5)
    elif a>=12:
        print("lisence suspended")
    print(a)
speed=int(input("enter the number:"))
my_function(speed)






























# def driver_license(speed):
#     if speed<70:
#         print("70")
#     elif speed>70:
#         i=71
#         j=0
#         while i<=speed:
#             if i%5==0:
#                 j+=1
#             i+=1
#         if j>12:
#             print("license suspended")
#         else:
#             print(j)
# driver_license(85)
# driver_license(135)