import keyword
kelist=keyword.kwlist
print(len(kelist))

# x,y,z=input().split()
# print(x,y,z)

val='This'[::-1]
print(val)
revStr1=""
def reverse(s):
    revStr=""
    for str in s.split():
        revStr+=str[::-1]+'$'
    return revStr


import os
import json as js
my_details = {

    "Name" : "Lalit Salunkhe",

    "Age" : 28,

    "Job" : True,

    }
obj=js.dumps(my_details)lis
print(obj)

#print(os.getcwd())

lis=[1,2,3,"India",[1,2,3]]
print(lis)

lis.append(24)
lis.remove(3)
print(lis)        
lis.pop()
print(lis)

lis.insert(2,10)
print(lis)
    
se=set(1,2,3)
print(se)


str="This is start for me"

# for str in Str:
#     print(str)

print(str[1:9])
print(str[:-2])