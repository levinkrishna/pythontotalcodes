from json import load
with open("C:\\Users\\Admin\\Desktop\\python_code\\mypython.py\\moviedb\\mdb.json","r",encoding="utf-8")as f:
    data=load(f)
#total num of movies
#print(len(data))


#print all movie names
# movie_names=[m.get("title")for m in data]
# print(movie_names)


#print movie with highest run time

# highest_numtimemovie=max(data,key=lambda m:int(m.get("runtime")))
# print(highest_numtimemovie)

#print all genres
# all_genres={g for m in data for g in m.get("genres")}
# print(all_genres)

#print movie name which contain genres comedy
# comedy_movies=[m.get("title") for m in data if "Comedy" in m.get("genres")]
# print(comedy_movies)




#print movie name which contain genres comedy or fantasy

genre_filter=[m.get("title")for m in data for g in m.get("genres") if g=="Comedy" or g=="Fantasy"]
print(genre_filter)

#yearwise movie count(1985:5,1984:3)

yc={}
for m in data:
    year=m.get("year")
    if year in yc:
        yc[year]+=1
    else:
        yc[year]=1
print(yc)


print(max(yc,key=lambda k:yc.get(k)))
print(min(yc,key=lambda k:yc.get(k)))

