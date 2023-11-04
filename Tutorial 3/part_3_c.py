cost=int(input("Enter cost of the meal :"))
sat_lev=input("1 = Total satisfied \n2 = Satisfied\n3 = Dissatisfied\nSatisfaction level :")

if sat_lev == "1":
    tip_lev=20
    sat="Totally satisfied"
elif sat_lev == "2":
    tip_lev=15
    sat="Satisfied"
else:
    tip_lev=10
    sat="Dissatisfied"

tip=cost*tip_lev/100


print("Satisfaction level: ",sat)
print("Tip: ",tip)
