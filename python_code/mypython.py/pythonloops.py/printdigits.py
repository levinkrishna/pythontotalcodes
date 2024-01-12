# program to print digits in a number

#num=123
#while(num!=0):#123 !=0 12!=0 1!=0
# digit=num%10 #3 2 1
# print(digit)#3  2 1
# num=num//10 #12 1



 #sum of digit in a given number

#num=153
#sum=0
#while(num!=0):
# digit=num%10
# sum=sum+digit
# num=num//10
#print(sum)




#amstrong number

num=123
orginal=num
count=len(str(num))
sum=0
while(num!=0):
 digit=num%10
 sum=sum+digit**count
 num=num//10
if(sum==orginal):
 print("amstrong number")
else:
 print("not amstong number")