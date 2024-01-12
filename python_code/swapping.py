num1=10
num2=20
print(f" values before swapping num1 {num1} num2 {num2}")
#logic 1
#temp=num1
#num1=num2
#num2=temp
#logic2
# (num1,num2)=(num2,num1)
#logic 3
num1=num1+num2
num2=num1-num2
num1=num1-num2
print(f" values after swapping num1={num1} num2={num2}")