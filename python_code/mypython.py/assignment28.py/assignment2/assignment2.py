# question 1


lst=[]
for i in range(1,4):
    name=input(f"Enter the Name of {1} person :")
    lst.append(name)
flag=1
while(flag==1):
    q=input("Do you want to invite more people ?: ")
    q1=q.lower()
    if q1=="yes":
        name=input(f"Enter the Name of person you want to invite: ")
        lst.append(name)
    else:
        print(f"{len(lst)} peoples are invited to the party")
        print("The invited peoples are: ")
        for n in lst:
            print(n)
        flag=0


# question 2


lst=[]
for i in range(1,4):
    name=input(f"Enter the Name of {1} person :")
    lst.append(name)
flag=1
while(flag==1):
    q=input("Do you want to invite more people ?: ")
    q1=q.lower()
    if q1=="yes":
        name=input(f"Enter the Name of person you want to invite: ")
        lst.append(name)
    else:
        print(f"{len(lst)} peoples are invited to the party")
        print("The invited peoples are: ")
        for n in lst:
            print(n)
        flag=0

q2=input("Enter the name of one person from above list: ")
q2=q2.lower()
pos=lst.index(q2)
print("Position of the selected person in list: ",pos+1)

q3=input("Do you still want that person to come to the party ?: ")
q3=q3.lower()
if q3=="no":
    lst.remove(lst[pos])
    print("New list :",lst)
else:
    print("New list :",lst)


# question 3

lst=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

for i in range(len(lst)):
    row=int(input("enter the row num : "))
    print(lst[row])
    break
value=int(input("enter a value : "))
lst[row].append(value)
print(lst[row])


# question 4

persons=[]
for i in range(4):
    name=input("Enter your name: ")
    age=input("Enter your age: ")
    id=input("Enter your id: ")
    persons.append({"name":name,"age":age,"id":id})

view=input("Enter the name of the person from the list: ")
for p in persons:
    if p["name"]==view:
        print(f"Age: {p['age']},ID: {p['id']}")

# question 5


persons=[]
for i in range(4):
    name=input("Enter your name: ")
    age=input("Enter your age: ")
    id=input("Enter your id: ")
    wc={"name":name,"age":age,"id":id}
    persons.append(wc)
    wc.pop("id")
print(persons)



# question 6

books={
    "My Favourite Nature Stories":{"author":"Ruskin Bond","publication year":2012,"genre":"mystery"},
    "China: Confucius in the Shadow":{"author":"Poonam Surie","publication year":2012,"genre":"fantacy"},
    "My Unforgettable Memories":{"author":"Mamata Banerjee","publication year":2000,"genre":"Historical"},
    "The Wrong Enemy: America in Afghanistan":{"author":"Carlotta Gall","publication year":2000,"genre":"Historical"},
    "Walking With Giants":{"author":"G. Ramachandran","publication year":2020,"genre":"mystery"},
    "One Life is Not Enough":{"author":"Natwar Singh","publication year":2023,"genre":"Action"},
    "The God of Small Things":{"author":"Arundhati Roy","publication year":2020,"genre":"Adventure"}
}
# Add a new book to the catalog
newbook={"True Colours":{"author":"Adam Gilchrist","publication year":2003,"genre":"comedy"}}
books.update(newbook)
print("New book added: ",books,"\n")

# update the author of an existing book
for k,v in books.items():
    if k=="Walking With Giants":
        v["author"]="Neel Mukherjee"
print("Author updated: ",books,"\n")

# Write a function to count how many books in the catalog were published before a given year.
def yearcount(years,date):
    count = 0
    for y in years:
        if y < date:
            count += 1
    return count

years=[]
for b,v in books.items():
    years.append(v["publication year"])
count=yearcount(years,2020)
print("Books that published before 2020: ",count)