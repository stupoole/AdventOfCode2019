import numpy as np


# Function to calculate fuel required to move mass according to f = floor(m/3)-2
def calculate_fuel(m):
    res = np.floor(m / 3) - 2
    if res <= 0:
        res = 0
    return res


# Load the input_masses
file_token = open("input.txt", "r")
in_masses = np.loadtxt(file_token)
file_token.close()

# Loops through each mass calculating each mass required for each module and then the mass required for it's fuel.
out_mass = 0
for mass in in_masses:
    work_mass = mass
    while work_mass > 0:
        work_mass = calculate_fuel(work_mass)
        out_mass += work_mass

print(out_mass)
