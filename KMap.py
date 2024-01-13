Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
class CASE:
    def __init__(self,L,V=Alpha):
        self.L = L
        self.V = V
    def __repr__(self,out="out"):
        s = 'else if('
        for i in range(len(self.L)):
            if self.L[i] == 1:
                s += "(" + self.V[i] + "==1) & "
            elif self.L[i] == 0:
                s += "(" + self.V[i] + "==0) & "
        s = s[:-3]
        s += f")\n    assign {out} = 1;"
        return s
    def contains(self,other):
        if len(self.L) != len(other.L):
            print("Mismatch in shape")
            return
        for i in range(len(self.L)):
            if self.L[i] == other.L[i]:
                continue
            elif self.L[i] is None:
                continue
            else:
                return False
        return True
    
    def __getitem__(self,i):
        return self.L[i]
    
    def __setitem__(self,i,x):
        self.L[i] = x

    def __len__(self):
        l = 0
        for x in self.L:
            if x is not None:
                l += 1
        return l

    def __eq__(self,other):
        if len(self.L) != len(other.L):
            print("Mismatch")
            return False
        for i in range(len(self.L)):
            if self.L[i] != other.L[i]:
                return False
        return True

    def reduce_using(self,L):
        toremove = []
        for i in range(len(self.L)):
            if self[i] is None:
                continue
            else:
                self[i] = 1-self[i]
            for j in range(len(L)):
                l = L[j]
                if l is self:
                    continue
                if l.contains(self):
                    if self == l:
                        toremove.append(j)
                    self[i] = None
                    break
            if self[i] is not None:
                self[i] = 1-self[i] 
        return sorted(list(set(toremove)))


def reduce(L):
    i = 0
    while i < len(L):
        #print(" + ".join([str(x) for x in L]))
        toremove = L[i].reduce_using(L)
        dec = len([j for j in toremove if j<=i])
        i -= dec
        for j in toremove[::-1]:
            L.pop(j)
        i += 1
    return L

def binary(x,bitcount=5):
    L = []
    for _ in range(bitcount):
        y = x%2
        L = [y] + L
        x = x//2
    return L

L = []
for P in range(1,10):
    for A in range(32):
        if A%P == 0:
            L.append(32*P + A)

cases = []
for x in L:
    c = CASE(binary(x,10),["P[4]","P[3]","P[2]","P[1]","P[0]","A[4]","A[3]","A[2]","A[1]","A[0]"])
    cases.append(c)
RC = reduce(cases)
for i in range(len(RC)):
    x = RC[i]
    print(x)
#s = "or(out"
#for i in range(len(RC)):
#    s += ",out" + str(i) 
#s += ");"
#print(s)


