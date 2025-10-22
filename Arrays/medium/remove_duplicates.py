#remove duplicates from sorted array
a=[1,2,3,4,5,5,6,7,7,7,8]
unique = []
for i in range(len(a)):
    if i==0 or a[i]!=a[i-1]:
        unique.append(a[i])
print(unique)

#using two pointer method

a=[1,2,3,4,4,5,6,7,8]
i=0

for j in range(1,len(a)):
    if a[j]!=a[i]:
        i+=1
        a[i]=a[j]
print(a[:i+1])
print(i+1)