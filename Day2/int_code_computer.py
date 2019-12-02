# in_program[i] is the opcode.
# following values are the positions of the parameters eg for add and mult:
#   in_program[i+1] is the position of the input a
#   in_program[i+2] is the position of the input b
#   in_program[i+3] is the position of the output


def int_code_computer(input_string):
    ended_safely_ = False
    i = 0
    while not ended_safely_:
        if input_string[i] == 1:  # add
            input_string[input_string[i + 3]] = input_string[input_string[i + 1]] + input_string[input_string[i + 2]]
            i += 4
        elif input_string[i] == 2:  # multiply
            input_string[input_string[i + 3]] = input_string[input_string[i + 1]] * input_string[input_string[i + 2]]
            i += 4
        elif input_string[i] == 99:  # end
            ended_safely_ = True
            break
        else:
            print("something went wrong")
    return input_string, ended_safely_
