#create a pattern
#sample input 1=num=2
#o/p
#2
#22
#sample input 1 num=3
#o/p
#3
#33
#333


num=3
for row in range(1,num+1):
   print(str(num)*row)

# by while
# num=6
# start=1
# while(start<=num):
#   print(str(num)*start)
#   start+=1