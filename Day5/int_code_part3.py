from int_code_computer import int_code_computer

with open("input_program.txt") as f:
    in_program = f.readlines()[0]

commands = list(map(int, in_program.split(',')))
int_code_computer(commands)


