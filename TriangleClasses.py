class TG_Vuong:
    def __init__(self, vuong1, vuong2, huyen):
        self.vuong1=vuong1
        self.vuong2=vuong2
        self.huyen=huyen
    def check(self):
        if(self.vuong1**2+self.vuong2**2==self.huyen**2):
            return False
        return True
li=[int(i) for i in input().split()]
li.sort()
TG=TG_Vuong(li[0], li[1], li[2])
if(TG.check()):
    print("INVALID")
else:
    print(li[0]+li[1]+li[2], float(li[1]*li[2]/2))