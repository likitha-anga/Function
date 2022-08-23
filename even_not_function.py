def add():
    list1=[2, 6, 18, 10, 3, 75]
    list2=[6, 19, 24, 12, 3, 87] 
    i=0
    while i<len(list1):
        if list1[i] and list2[i]%2==0:
            print("both are even")
        else:
            print("both are not even")
        i+=1
add()
            
        
        