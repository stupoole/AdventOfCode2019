# in_program[i] is the opcode.
# following values are the positions of the parameters eg for add and mult:
#   in_program[i+1] is the position of the input a
#   in_program[i+2] is the position of the input b
#   in_program[i+3] is the position of the output


def int_code_computer(input_string):
    ended_safely_ = False
    i = 0
    while not ended_safely_:
        opcode = input_string[i] % 100  # Last 2 digits
        param_modes = input_string[i] // 100  # first n-2 digits
        param_mode_a = param_modes % 10
        param_mode_b = (param_modes // 10) % 10
        # param_mode_c = (param_modes // 100) % 10
        print(input_string[i], opcode, param_modes)

        if opcode == 1:  # add
            if param_mode_a == 1:
                param_a = input_string[i + 1]
            else:
                param_a = input_string[input_string[i + 1]]

            if param_mode_b == 1:
                param_b = input_string[i + 2]
            else:
                param_b = input_string[input_string[i + 2]]
            input_string[input_string[i + 3]] = param_a + param_b
            i += 4

        elif opcode == 2:  # multiply
            if param_mode_a == 1:
                param_a = input_string[i + 1]
            else:
                param_a = input_string[input_string[i + 1]]

            if param_mode_b == 1:
                param_b = input_string[i + 2]
            else:
                param_b = input_string[input_string[i + 2]]
            input_string[input_string[i + 3]] = param_a * param_b
            i += 4

        elif opcode == 3:  # take input
            input_string[input_string[i + 1]] = int(input('Please supply an integer: '))
            i += 2

        elif opcode == 4:  # output
            print('diagnostic code: ', input_string[input_string[i + 1]])
            i += 2

        elif opcode == 5:  # jump if true
            if param_mode_a == 1:
                param_a = input_string[i + 1]
            else:
                param_a = input_string[input_string[i + 1]]
            if param_mode_b == 1:
                param_b = input_string[i + 2]
            else:
                param_b = input_string[input_string[i + 2]]
            if param_a != 0:
                i = param_b
            else:
                i += 3

        elif opcode == 6:  # jump if false
            if param_mode_a == 1:
                param_a = input_string[i + 1]
            else:
                param_a = input_string[input_string[i + 1]]
            if param_mode_b == 1:
                param_b = input_string[i + 2]
            else:
                param_b = input_string[input_string[i + 2]]
            if param_a == 0:
                i = param_b
            else:
                i += 3

        elif opcode == 7:  # less than
            if param_mode_a == 1:
                param_a = input_string[i + 1]
            else:
                param_a = input_string[input_string[i + 1]]
            if param_mode_b == 1:
                param_b = input_string[i + 2]
            else:
                param_b = input_string[input_string[i + 2]]
            param_c = input_string[i + 3]
            if param_a < param_b:
                input_string[param_c] = 1
            else:
                input_string[param_c] = 0
            i += 4

        elif opcode == 8:  # Equals
            if param_mode_a == 1:
                param_a = input_string[i + 1]
            else:
                param_a = input_string[input_string[i + 1]]
            if param_mode_b == 1:
                param_b = input_string[i + 2]
            else:
                param_b = input_string[input_string[i + 2]]
            param_c = input_string[i + 3]
            if param_a == param_b:
                input_string[param_c] = 1
            else:
                input_string[param_c] = 0
            i += 4

        elif opcode == 99:  # end
            ended_safely_ = True
            break

        else:
            print("something went wrong")
            break
    return input_string, ended_safely_
