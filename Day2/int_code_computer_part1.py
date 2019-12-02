import numpy as np
import int_code_computer

# Load the input program
file_token = open("input_programming.txt", "r")
in_program = np.loadtxt(file_token, delimiter=',', dtype=np.int64)
file_token.close()
in_program[1] = np.int64(12)
in_program[2] = np.int64(2)

out_program, status = int_code_computer(in_program)
if status:
    print(out_program[0])
else:
    print("Failed")
