#num=10
#print("+ve" if num>0 else "-ve")

#print("odd"if num%2!=0 else "even")

#num1=100
#num2=20
#print("largest number is",num1 if num1>num2 else num2)



#ternary operator

#def max_two(n1,n2):
 #   return n1 if n1>n2 else n2
#print(max_two(100,20))

#def min_two(n1,n2):
#    return n1 if n1<n2 else n2
#print(min_two(100,20))

def max_three(n1,n2,n3):
   return n1 if (n1>n2) and (n1>n3)  else n2  if(n2>n3) else n3
print(max_three(10,2,30))