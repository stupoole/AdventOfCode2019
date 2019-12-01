import numpy as np

def calculate_fuel(m):
    res = np.floor(m/3) - 2
    if res <= 0:
        res = 0
    return res

file_token = open("input.txt", "r")

in_masses = np.loadtxt(file_token)
file_token.close()


out_mass = 0
for mass in in_masses:
    work_mass = mass
    while work_mass > 0:

        work_mass = calculate_fuel(work_mass)
        out_mass += work_mass


print(out_mass)

