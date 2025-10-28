#moving all zeros in an array to the end of an array

a = [1,0,5,0,7,3,0,4,0]
j = 0
for i in range(len(a)):
    if a[i]!=0:
        a[j],a[i]=a[i],a[j]
        j+=1
    