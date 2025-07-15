day = 4
match day:
    case 1:
            print("Monday")
    case 2:
            print("Tuesday")
    case 3:
            print("wednesday")
    case 4:
            print("Thursday")
    case 5:
            print("Friday") 
    case 6:
            print("Saturday")
    case 7:
            print("Sunday")

# Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches
day=4
match day:
    case 5:
            print("Friday") 
    case 6:
            print("Saturday")
    case 7:
            print("Sunday")
    case _:
            print("Hey it's Tuesday")

#Combining values using union operator
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")


month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")