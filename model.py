import numpy as np
import math
import random


def RG_Single_exp(dt, m, gamma, x0, y0, v0, kT=1, U0=3):
    fac_randy = math.sqrt(2*kT/dt)
    fac_randy=math.sqrt(2*kT/dt)
    fac_pot=4*U0

    xx=x0
    yy=y0
    vv=v0
    state=True
    x = 0.
    ffpt = 0.
    while state==True:
        xi = random.gauss(0.0, 1.0)
        fr = fac_randy*xi

        kx1 = dt*vv
        kv1 = dt * (1/gamma*(yy-xx) - fac_pot*(xx**3-xx))/m
        ky1 = dt * (1/gamma*(xx-yy) + fr)
        
        x1 = xx + kx1/2
        v1 = vv + kv1/2
        y1 = yy + ky1/2

        kx2 = dt*v1
        kv2 = dt * (1/gamma*(y1-x1) - fac_pot*(x1**3-x1))/m
        ky2 = dt * (1/gamma*(x1-y1) + fr)
        
        x2 = xx + kx2/2
        v2 = vv + kv2/2
        y2 = yy + ky2/2



        kx3 = dt*v2
        kv3 = dt * (1/gamma*(y2-x2) - fac_pot*(x2**3-x2))/m
        ky3 = dt * (1/gamma*(x2-y2) + fr)
        
        x3 = xx + kx3
        v3 = vv + kv3
        y3 = yy + ky3


        kx4 = dt*v3
        kv4 = dt * (1/gamma*(y3-x3) - fac_pot*(x3**3-x3))/m
        ky4 = dt * (1/gamma*(x3-y3) + fr)
        
        x0 = xx
        # Record the previous step
        xx += (kx1 + 2*kx2 + 2*kx3 + kx4)/6
        vv += (kv1 + 2*kv2 + 2*kv3 + kv4)/6
        yy += (ky1 + 2*ky2 + 2*ky3 + ky4)/6

        if xx>1:
            #transfer to another state 1
            state = False
            v = (xx-x0)/dt
            x = 1-x0
            t = x/v
            ffpt += ffpt+t 
        else:
            ffpt += dt

    return ffpt

