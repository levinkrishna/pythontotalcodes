items=[
    [1,"potatto",45,"veg",10],
    [1,"tomatto",40,"veg",20],
    [1,"onion",35,"veg",0],
    [1,"brinjal",50,"veg",0],
    [1,"fish",145,"nonveg",10],
    [1,"chicken",145,"nonveg",10],
    [1,"egg",6,"nonveg",100]
 
    
]

# total number products
print(len(items),"items")

# print in stock product names

in_stock=[item[1] for item in items if item[4]!=0]
print(in_stock)

# print out of stock product names

out_of_stock=[item[1] for item in items if item[4]==0]
print(out_of_stock)
# print veg category product names

veg=[item[1] for item in items if item[3]=="veg"]
print(veg)

# product available in range of 50-100

items_in_range=[item[1] for item in items if(item[2] in range (50,101))]
print(items_in_range,"range of 50,100")


# veg products available in range of 40-80

veg_products=[item[1] for item in items if(item[3]=="veg") if(item[2] in range(40,80))]

print(veg_products)

