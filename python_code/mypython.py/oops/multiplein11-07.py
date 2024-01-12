class P1:
    def m1(self):
        print("class p1 m2 method")

class P2:
    def m2(self):
        print("class p2 m2 method")

class c1(P2,P1):
    pass

c=c1()
c.m1()