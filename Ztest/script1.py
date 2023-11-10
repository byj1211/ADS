
E=EllipticCurve(Zmod(n),[a,b])
P1=E(C1)
P2=E(C2)
P3=E(C3)
# 三个e的ECRSA共模攻击
g1,s1,t1=xgcd(e1,e2)
g2,s2,t2=xgcd(g1,e3)
assert g2 == 1
M=s2*s1*P1 + s2*t1*P2 + t2*P3
from Crypto.Util.number import *
print(long_to_bytes(int(M[0])))