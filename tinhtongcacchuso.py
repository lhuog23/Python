
t= int(input())
while t>0:
    s= input()
    sum=0
    s1=''
    for i in range(0,len(s)):
        if s[i].isalpha():
            s1+= s[i]
        else:
            sum+= int(s[i])
    s2=sorted(s1)
    d=''.join(s2)
    # print(d+str(sum))
    print(d)
    t-=1