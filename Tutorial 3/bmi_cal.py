weight = int(input('Weight(kilograms) : '))
height = float(input('Height(meters)    : '))
bmi =weight / height**2
print('Your BMI value is', bmi)



if bmi <= 18.5 :
    bmi_cat = 'Under weight'
elif 18.5<bmi<=24.9 :
    bmi_cat = 'Normal weight'
elif 25<=bmi<=29.9 :
    bmi_cat = 'Over weight'
elif bmi>=30 :
    bmi_cat = 'Obesity'

print ('BMI Category :', bmi_cat)


