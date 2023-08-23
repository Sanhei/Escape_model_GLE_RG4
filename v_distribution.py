import numpy as np
import random

import matplotlib.pyplot as plt
# Create function dictionary
function_dict = {}

# 1. constant
class constant:
    def generator(mass):
            return 0
function_dict["const"] = constant

# 2. Gaussian
class gaussian:
    def generator(mass):
        return random.gauss(0, mass)
function_dict["gauss"] = gaussian

# 3. Flux maxwell distribution
'''
P(v)∝v*exp(-mv^2/2kBT)
normalize:∫P(v)dv=1/m
P(v)=1/m*v*exp(-mv^2/2kBT)
Using Monte Carlo to simulate this probability
'''
def flux_max_func(x, mass):
    return mass/2*abs(x)*np.exp(-1/2*mass*x**2)
class flux_maxwell():
    def generator(mass):
        while(True):
            x = random.uniform(0, 1)
            v = random.uniform(-10/mass, 10/mass )
            if flux_max_func(v, mass)>=x:
                return v

function_dict["flux_maxwell"] = flux_maxwell


def create_distribution(function_name):
    if function_name in function_dict:
        return function_dict[function_name]
    else:
        assert False, f"Unknown function name \"{function_name}\", available function are {str(function_dict.key())}"


class initial_velocity_distribution:
    def __init__(self, function_name):
        self.function_name=function_name
        self.distribution = create_distribution(function_name)
    def generator(self, mass):
        return self.distribution.generator(mass)


