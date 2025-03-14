a=int(input("Enter a number:"))
c=[]
while a>=1:
    b=a%2
    c.append(b)
    a//=2
print(c[::-1])
