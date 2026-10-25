from fractions import Fraction as F

def orbit_1d(p, radius=5, L=F(1)):
    return {2*n*L+sg*p for n in range(-radius,radius+1) for sg in (-1,1)}

def folded(x,L=F(1)):
    # Invariant of the infinite mirror orbit for rational data
    y=x%(2*L)
    return min(y,2*L-y)

p=F(1,4)
o=orbit_1d(p,10)
assert F(7,4) in o
assert F(3,4) not in o
assert F(5,4) not in o
assert all(folded(x)==p for x in o)
assert folded(F(3,4))==F(3,4)
assert folded(F(5,4))==F(3,4)
assert orbit_1d(F(3,4),10).isdisjoint(o)
for scale in [F(1,2), F(1), F(3), F(17,5)]:
    for x in o:
        assert folded(scale*x,scale)/scale == folded(x)
# New mirror plane b=3/4 reflects 1/4 to 5/4
assert 2*F(3,4)-p==F(5,4)
print('O59 verificación racional: PASS (8 grupos de verificaciones)')
