# guesses: 1717892 too high, 36323 too low, 43812!

from itertools import permutations
from int_code_computer import IntCodeComputer

with open("amplifier_program.txt") as f:
    in_program = f.readlines()[0]

x = [0, 1, 2, 3, 4]
myCombinations1 = list(map(list, permutations(x, 5)))
commands = list(map(int, in_program.split(',')))
pairings = dict()
phases = list(list())
for combination in myCombinations1:
    output = 0
    for phase in combination:
        amplifier = IntCodeComputer(commands.copy())
        output_program, output = amplifier.run([phase, output])
    pairings[output] = combination
print("part1 : ", max(pairings.keys()))

# x = [5, 6, 7, 8, 9]
# myCombinations2 = list(map(list, permutations(x, 5)))
# commands = list(map(int, in_program.split(',')))
# pairings = dict()
# phases = list(list())
# for combination in myCombinations2:
#     output = 0
#     for phase in combination:
#         amplifier = IntCodeComputer(commands.copy())
#         output_program, output = amplifier.run([phase, output])
#     pairings[output] = combination
#
# print("part2 : ", max(pairings.keys()))
