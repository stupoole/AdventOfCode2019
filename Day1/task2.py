import numpy as np


def calculate_fuel_vect(m):
    res = np.floor(m / 3) - 2
    res[res <= 0] = 0
    return res


# Load the input_masses
file_token = open("input.txt", "r")
in_masses = np.loadtxt(file_token)
file_token.close()

# Vectorised version of calculating masses
out_mass = 0
work_mass = in_masses.copy()
while np.sum(work_mass) > 0:
    work_mass = calculate_fuel_vect(work_mass)
    out_mass += np.sum(work_mass)

print(out_mass)
