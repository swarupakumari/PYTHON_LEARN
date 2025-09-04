day = 3
# there is no requirement for writing break keyword like other eg cpp mai switch case
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")
        
        # using if else in match case
num = 18

match num:
    case n if n < 0:
        print("Number is negative.")
    case n if 1 <= n <= 10:
        print("Number is between 1-10")
    case n if 11 <= n <= 20:
        print("Number is between 11-20")
    case n if n > 20:
        print("Number is greater than 20")
    case 0:
        print("Number is zero")
 