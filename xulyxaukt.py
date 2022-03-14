t= int(input())
def ptsn(n):
    i= 2
    lst=[]
    while n>1:
        if(n%i==0):
            n= int(n/i)
            lst.append(i)
        else:
            i+=1
    if len(lst)==0:
        lst.append(n)
    return lst
while t>0:
    n= int(input())
    m=1
    lst=ptsn(n)
  
    d=''.join(lst(x) for x in lst)
    print(d)
    size= len(lst)
    sum=0
    for i in range(0,size-1):
        sum+= int(lst[i])
    print(sum)
    t-=1
