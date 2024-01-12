items = [
    {"sugar": 45},
    {"tea_powder": 28},
    {"coffee": 67},
    {"dairymilk": 170},
    {"kitkat": 70},
    {"bourborn": 50},
    {"munch": 30},
    {"milk": 80},
    {"pepsi": 99},

]

offers=[
    {"sugar":10},
    {"cofee":20},
    {"milk":5},
    {"pepsi":10}
]
# for i in items :
#  for o in offers:
#      for key in i.keys():
#          if key in o:
#              discount=o[key]
#              selling_price=i[key]-discount
#              print(selling_price)
wc={}
for i in items:
    for o,i in i.items():
        wc[o]=i
off={}
for v in offers:
    for a,b in v.items():
        off[a]=b
for n,m in off.items():
    itemname=n
    value=m
    if itemname in wc:
     wc[itemname]-=m
print(wc)


