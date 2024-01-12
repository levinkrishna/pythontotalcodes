allusers=["mohanlal","fahad","dq","vijay","nivin","asif"]
dq_friendlist=["mohanlal","fahad","asif"]
asif_friendlist=["mohanlal","fahad","vijay","nivin"]
#suggestion for dq
users=set(allusers)
dqfriends=set(dq_friendlist)
suggestion_for_dq=users.difference(dqfriends)
suggestion_for_dq.remove("dq")
print(suggestion_for_dq)

#or


"""suggestions=set(allusers).difference(set(dq_friendlist))
suggestions.remove("dq")
print(suggestions)"""

#mutual friendsof dq and asif

mutual_friends=set(dq_friendlist).intersection(set(asif_friendlist))
print(mutual_friends)
