weight=65
height=154
heightinmtr=(height)/(100)
bmi=weight/heightinmtr**2
print(bmi)
if(bmi<=18.5):
 print("under_weight")
elif(bmi<=24.9):
 print("normal_weight")
elif(bmi<=29.9):
 print("over_weight")
elif(bmi<=34.4):
 print("obesity leval_1")
elif(bmi<39.9):
 print("obesity_leval_2")
else:
 print("obesity_leval_3")
 