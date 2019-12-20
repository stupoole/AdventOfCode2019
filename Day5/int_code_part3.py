from int_code_computer import IntCodeComputer

with open("input_program.txt") as f:
    in_program = f.readlines()[0]

commands = list(map(int, in_program.split(',')))
TEST = IntCodeComputer(commands)

print(TEST.run([5])[1])

