def maximum(list):
    i=0
    maximum=0
    while i<len(list):
        if list[i]>maximum:
            maximum=list[i]
        i+=1
    print(maximum)
list= [3, 5, 7, 34, 2, 89, 2, 5]
maximum(list)


