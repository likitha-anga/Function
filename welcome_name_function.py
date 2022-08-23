def my_function(party):
    a=party
    print(a)
my_function("welcome")
my_function("sonu")
my_function("monu")
    
    
d={1:2,2:3,3:4,4:5}
a=[]
for x in d.keys():
    if x in a:
        continue
    else:
        a.append(x)
print(a)
  