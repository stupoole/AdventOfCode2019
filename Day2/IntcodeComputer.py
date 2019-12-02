import numpy as np

# Load the input program
file_token = open("input_programming.txt", "r")
in_program = np.loadtxt(file_token, delimiter=',', dtype=np.int64)
file_token.close()
in_program[1] = np.int64(12)
in_program[2] = np.int64(2)
i = np.int(0)
while in_program[i] != 99:
    opcode = in_program[i]
    in_a_pos = in_program[i + 1]
    in_b_pos = in_program[i + 2]
    out_pos = in_program[i + 3]
    if in_program[i] == 1:
        in_program[out_pos] = in_program[in_a_pos] + in_program[in_b_pos]

    elif in_program[i] == 2:
        in_program[out_pos] = in_program[in_a_pos] * in_program[in_b_pos]
    else:
        print("something went wrong")
    i += 4

print(in_program[0])
