message="hello World!"
print(message.strip())#Strip method is used to delete the begin and end spaces of a string.

print(message.split())#split() method is used for spliting string and making a list.

print(message.upper())#upper method is used for  converting the whole string uppercase.

print(message.lower())#lower method is used for converting the whole string to lowercase.

print(message.capitalize())#Which helps to capitalize the frist character of a string.

print(message.title())#title() is udes for converts the first character to upper case and rest to lower case.

print(message.swapcase())#Which converts lowercase letter into uppercase and vice-versa

print(message.center(20,"-")) #the word "hello" is centered within a 20-character wide space

print(message.count("l")) #Count() which helps to the count of occurence

s = "GEEKSFORGEEKS"
print(s.isupper())

s1 = "HelloWorld"
res1 = s1.isalpha()
print(res1)


a = "shakshi" # name 
b = 22 # age

msg = "My name is {0} and I am {1} years old.".format(a,b)
print(msg)