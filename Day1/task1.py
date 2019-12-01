import numpy as np

# Load the input files
file_token = open("input.txt", "r")
in_masses = np.loadtxt(file_token)
file_token.close()

# calculate fuel: fuel = floor(mass/3)-2
out_mass = np.sum(np.floor(in_masses/3)-2)
print(out_mass)