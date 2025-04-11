#using slice() method
string = 'Coding Ninjas'
print(string[slice(6)])

string = 'Coding Ninjas'
print(string[slice(2,10)])

string = 'Coding Ninjas'
print(string[slice(-10,-3)])

#using list
string = 'Coding Ninjas'
print(string[3:9])

list=[1,2,3,4,5,6.7,8,9,10]

list_1=list[5:9]
print(list_1)

list_2=list[1::2]
print(list_2)

list_3=list[1::]
print(list_3)
