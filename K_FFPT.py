# This program is based on the Henrike code developed
# https://www.physik.fu-berlin.de/en/einrichtungen/ag/ag-netz/group-members/phd-students/kiefer/index.html

'''
The goal is to simulate the Kramers problem.
By giveing different initial velocity distribution, we record
the first-to-first passage time.

where the state boundary is defined as 1 in model.py, if xx>1:
'''

import numpy as np
import math

from model import RG_Single_exp 

import argparse
import multiprocessing



parser = argparse.ArgumentParser(description='Particle escape time by GLE in double well potential')
# The special character made by HEX code.
parser.add_argument('mass', metavar='m', type=float, help="Mass τₘ/τ_D")
parser.add_argument('timestep', metavar='dt', type=float, help="The simulation time step(dt)")
parser.add_argument('Memory',  metavar='g', type=float, help='Memory time τ_Γ')
parser.add_argument('filepath', metavar='f', 
        type=str, default="ffpt.txt", help='Save file path +.txt')
parser.add_argument('N_transition', metavar='N', 
        type=int, default=int(1e6), help='Number of state transitions')

args = parser.parse_args()


print("Mass is ", args.mass, "dt is ", args.timestep, 
        "Memory time is ", args.Memory, "Number of transitions ", args.N_transition)

# Multicore function preparation.
def Multicore_RG(N):
    return RG_Single_exp(args.timestep, args.mass, args.Memory, x0=-1, y0=0, v0=0, kT=1, U0=3)

pool_obj = multiprocessing.Pool()
FFPT = pool_obj.map(Multicore_RG, range(args.N_transition))

FFPT = np.array(FFPT)
np.savetxt(args.filepath, FFPT)





