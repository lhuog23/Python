tong = 0
tich = 1
check = False

n = int (input ())

if (n >= 0 and n <= 10):
    for i in range (0,n):
        a, b = map (str, input ().split ())
        if b.isdecimal () == True:
            tong += int (b)
            tich *= int (b)
            check = True
    if check == True:
        print (tong, tich)
    else:
        print ("INVALID INPUT")    
else:
    print ("INVALID INPUT")