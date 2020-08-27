num=int(input())
person=[]
p=input().split()
for i in range(num):
    person.append(p[i])

m=int(input())
book_dict={name:0 for name in person}
for i in range(m):
    sp=input().split()
    name=sp[0]
    money=int(sp[1])
    
    book_dict[name]+=money
    

book_sorted=sorted(book_dict.items(),key=lambda x:x[1] ,reverse=True)
for i in range(num):
    print(book_sorted[i][0])  
