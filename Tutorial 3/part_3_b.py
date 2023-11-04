num_1 = int(input("Enter number 1: "))
operator = input("Operator: ")
num_2 = int(input("Enter number 2: "))
try:
    
    if operator=="+":
        ans=num_1+num_2
    elif operator=="-":
        ans = num_1 - num_2
    elif operator=="*":
        ans= num_1 * num_2
    elif operator=="/":
        ans = num_1 / num_2

    print(num_1 ,operator ,num_2 ,"=", ans)

except ZeroDivisionError :
    print ("You can't devide number by Zero ! ")
