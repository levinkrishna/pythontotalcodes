mob={"id":1000,"name":"apple","price":30000}

# if ("price in mob "):
#     print(mob["price"])

for key in mob:
    print(key,mob[key])

    #add new key value pair
mob["display"]="amoled"
print(mob)

# add 500 rs discount in price

mob["price"]-=500
print(mob)
