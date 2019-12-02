import numpy as np
from int_code_computer import int_code_computer


# Loops through all possible noun, verb pairings
def test_pairings():
    for noun in range(0, 100):
        for verb in range(0, 100):
            temp_program = in_program.copy()  # reset the array
            temp_program[1] = noun
            temp_program[2] = verb

            out_program, status = int_code_computer(temp_program)

            if out_program[0] == np.int64(19690720):
                return 100 * noun + verb


file_token = open("input_programming.txt", "r")
in_program = np.loadtxt(file_token, delimiter=',', dtype=np.int64)
file_token.close()

print(test_pairings())
