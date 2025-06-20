#Converting string to list
s="Coding is fun"
print(s.split())

def convert(s):
    list=s.split()
    return list
s="Coding is fun"
print(convert(s))

#using Slicing
def convert(s):
    list=[]
    list[:0]=s
    return list[5:12]
s="Coding is fun"
print(convert(s))

#using map
s="Coding is fun"
b=list(map(str,s))
print(b)

#using enumerate
s="Coding is fun"
b=list(enumerate(s))
print((b))

s="Coding is fun"
x=[n for a,n in enumerate(s)]
print(x)

#using list
s="Coding is fun"
lit=list(s)
print(lit)

#using Json.loads()
import json
s='["Coding", "is", "fun"]'
l=json.loads(s)
print(l)

#using strip
s="Coding is fun"
print(list(s.strip()))

#using lambda
s="Coding is fun"
res=list(filter(lambda x:(x in s),s))
print(res)
