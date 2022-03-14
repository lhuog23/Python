n = int(input())
for i in range(n):
    a=input()
    a=a.lower()
    if 't' not in a: 
        print("-1")
    else:
        li=[]
        for i in range(len(a)):
            if a[i]=='t': li.append(i)
        print(f"{li[0]} {li[1]} {li[-1]}")