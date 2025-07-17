#Using Swapcase()
lower_case="hey how are you"
case_1=lower_case.swapcase()
print(case_1)

Upper_case="HEY HOW ARE YOU"
case_2=Upper_case.swapcase()
print(case_2)

str="HEy HoW ArE yOu"

new_str=""
for letter in str:
    if(letter.isupper())==True:
        new_str+=(letter.lower())
    elif(letter.islower())==True:
        new_str+=(letter.upper())
    elif(letter.isspace())==True:
        new_str+=letter

print('Original String:', str)
print('Changed String:', new_str)


greeting="hey how are you @1235#$%"
case_3=greeting.swapcase()
print(case_3)

usernames = ['rahul_sharma', 'riya_soni', 'PETER_PARKER', 'rohit_sharma']

formatted_usernames = [username.capitalize() for username in usernames]

for username in formatted_usernames:
    print(username)