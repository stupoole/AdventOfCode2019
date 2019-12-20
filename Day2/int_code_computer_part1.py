import numpy as np
from int_code_computer import IntCodeComputer

# Load the input program
file_token = open("input_programming.txt", "r")
in_program = np.loadtxt(file_token, delimiter=',', dtype=np.int64)
file_token.close()
in_program[1] = np.int64(12)
in_program[2] = np.int64(2)
program_alarm = IntCodeComputer(in_program)
out_program, output = program_alarm.run([])

print(output)

