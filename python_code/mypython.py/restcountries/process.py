from json import load
with open("C:\\Users\\Admin\\Desktop\\python_code\\mypython.py\\restcountries\\rest.json",encoding="UTF-8")as f:
    data=load(f)
    # print(len(data))

#print all country names
# for c in data:
#  print(c.get("name"))

# all_country_names=[c.get("name") for c in data]
# print(all_country_names)


#print all region names

# all_regions={c.get("region") for c in data}
# print(all_regions)

#print asian country names

# asian_countries=[c.get("name")for c in data if c.get ("region")==("Asia")]
# print(asian_countries)

#print population of afganisthan

# afgn_population=[c.get("population")for c in data if c.get("name")==("Afghanistan")]
# print(afgn_population)


#indian borders

country_borders=[c.get("borders") for c in data if c.get("name")=="India"][0]

print(country_borders)

country_borders_names=[c.get("name") for c in data if c.get("alpha3Code") in country_borders]
print(country_borders_names)


#print currency code

# multi_currency_country=[for c in data if len(c.get("currencies"))>1]  incorrect question



