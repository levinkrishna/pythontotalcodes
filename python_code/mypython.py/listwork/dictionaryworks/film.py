movies={"2018":5,"keralastory":3,"neymar":4,"kgf":5,"arm":4}

#print all movie names

print(movies.keys())

#print top rated movie
print(max(movies,key=lambda k:movies.get(k)))


#sort movies wrt rating order by desc

out=sorted(movies,reverse=True,key=lambda k:movies.get(k))
print(out)