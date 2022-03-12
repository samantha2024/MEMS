import numpy as np

E0 = 8.85e-12
w = 120e-6	
W = 120e-6
g0 = 3e-6
E = 69e9
t = 1e-6
l = 400e-6
v = 0.33
s = 20e6	#residual stress

a = t/l
b = pow(a,3)
c = pow(g0,3)
A = w*W

kz = 0.5*( 32*E*w*b + 8*s*(1-v)*w*a)
print(kz)	#paper's kz = 18.41(comsol), 17.8(Theoretical Model)
Vp = np.sqrt( (8*kz*c) / (27*E0*A))
print(Vp)	#paper's Vp = 38.5V(comsol), 34V(Theoretical Model)
