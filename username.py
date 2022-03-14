from os import sep


t=  int(input())
lst=[]
while t>0:
    n= input().lower()
    if n not in lst:
        lst.append(n)

    t-=1
b= sorted(lst)
print(*b,sep="\n")