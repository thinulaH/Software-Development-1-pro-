x=int(input("Enter '1' if you want to C--->F \nEnter '2' if you want to F--->C \n"))
if x==1:
    c=int(input("Enter the temprature in Celsius: "))
    f=(c*1.8)+32
    print("Temprature in Fahrenheit: ", f)
elif x==2:
    f=int(input("Enter the temprature in Fahrenheit: "))
    c=(f-32)/1.8
    print("Temprature in Celsius: ", c)
else:
    print("Invalid option enterd")
