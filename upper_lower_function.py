# def function(string):
#     i=0
#     count1=0
#     count2=0
#     while i<len(string):
#         if string[i].isupper():
#             count1+=1
#         elif string[i].islower():
#             count2+=1
#         i+=1
#     print("upper_case=",count1)
#     print("lower_case=",count2)
# function("Likitha.Anga,InduMathi.Kosara")


def function(string):
    i=0
    count1=0
    count2=0
    while i<len(string):
        if string[i].isupper():
            count1+=1
        elif string[i].islower():
            count2+=1
        i+=1
    print("upper=",count1)
    print("lower=",count2)
function("likithaharshaAmaravathiGovindrao")
    
    