#functions are used to perform a specific task

#num1=input("enter value for num1 :")
#print(num1)

#create a function for adding two parameter and a return value
#def add(n1,n2):
 #   res=n1+n2
  #  return res
#print(add(15,25))

#create a function multiplication with 3 parameter

#def mulitiplication(n1,n2,n3):
#  res=n1*n2*n3
#  return res
#print(mulitiplication(2*3*2))


#Create a function max_two with two parameter that return largest num


# def max_two(n1,n2):
#    if(n1>n2):
#        return n1
#    else:
#        return n2
# print(max_two(100,20))

# num1=12
# num2=25
# print(num1 if num1>num2 else num2)



def factorial(num):
    fact=1
    for i in range (1,(num+1)):
     fact*=1
     return fact
print(factorial(4))
