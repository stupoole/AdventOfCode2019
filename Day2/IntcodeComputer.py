import numpy as np

# Load the input program
file_token = open("input_programming.txt", "r")
in_program = np.loadtxt(file_token, delimiter=',', dtype=np.int64)
file_token.close()
in_program[1] = np.int64(12)
in_program[2] = np.int64(2)
i = np.int(0)

# in_program[i] is the opcode.
# in_program[i+1] is the position of the input a
# in_program[i+2] is the position of the input b
# in_program[i+3] is the position of the output
while in_program[i] != 99:
    if in_program[i] == 1:
        in_program[in_program[i + 3]] = in_program[in_program[i + 1]] + in_program[in_program[i + 2]]

    elif in_program[i] == 2:
        in_program[in_program[i + 3]] = in_program[in_program[i + 1]] * in_program[in_program[i + 2]]
    else:
        print("something went wrong")
    i += 4

print(in_program[0])
