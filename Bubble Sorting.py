a=[8,3,2,21,52,43,6,95]
for i in range(len(a)-2):
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)
