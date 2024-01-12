users=["sachin","kohli","sehwag","dhoni","raina"]
sachin_followers=["kohli","sehwag","rahul"]
request_suggestion_sachin=[]
for suggestions in users:
   if suggestions!="sachin" and suggestions not in sachin_followers:
    request_suggestion_sachin.append(suggestions)
print(request_suggestion_sachin)