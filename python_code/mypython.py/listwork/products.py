mobiles=[
    [100,"redminote12",23000,"5g"],
    [101,"oneplusnord",32000,"5g"],
    [102,"iphnoe14",123000,"5g"],
    [103,"s23ultra",133000,"5g"],
    [104,"pexel12",43000,"5g"],
    [105,"nothing",13000,"4g"],
    [106,"galaxya52",23000,"5g"]
        
]
#print total number of mobiles
print(len(mobiles),"mobiles available")
#print all mobile names
mobile_name=[mob[1] for mob in mobiles]
print(mobile_name)
#print all 4g mobiles
mobile_name=[mob[1] for mob in mobiles if(mob[3]=="4g")]
print(mobile_name,"is 4g")

#print all mobile names price <30000
mobile_name=[mob[1] for mob in mobiles if(mob[2]<30000)]
print(mobile_name,"is less than 30000")
#print mobile names available in range of 30000 to 50000
mobile_name=[mob[1] for mob in mobiles if(mob[2] in range (30000,50000))]
print(mobile_name)
#print all mobile names avaible under 25000
mobile_name=[mob[1] for mob in mobiles if (mob[2]<25000)and mob[3]=="5g"]
print(mobile_name)
