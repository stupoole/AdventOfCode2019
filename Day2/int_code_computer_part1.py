import numpy as np
import int_code_computer

# Load the input program
file_token = open("input_programming.txt", "r")
in_program = np.loadtxt(file_token, delimiter=',', dtype=np.int64)
file_token.close()
in_program[1] = np.int64(12)
in_program[2] = np.int64(2)
ended_safely = False
i = 0

# in_program[i] is the opcode.
# following values are the positions of the parameters eg for add and mult:
#   in_program[i+1] is the position of the input a
#   in_program[i+2] is the position of the input b
#   in_program[i+3] is the position of the output

# while not ended_safely:
#     if in_program[i] == 1:  # add
#         in_program[in_program[i + 3]] = in_program[in_program[i + 1]] + in_program[in_program[i + 2]]
#         i += 4
#     elif in_program[i] == 2:  # multiply
#         in_program[in_program[i + 3]] = in_program[in_program[i + 1]] * in_program[in_program[i + 2]]
#         i += 4
#     elif in_program[i] == 99:  # end
#         ended_safely = True
#         break
#     else:
#         print("something went wrong")

out_program, status = int_code_computer(in_program)
if status:
    print(out_program[0])
else:
    print("Failed")
