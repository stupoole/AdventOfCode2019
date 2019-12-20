# in_program[i] is the opcode.
# following values are the positions of the parameters eg for add and mult:
#   in_program[i+1] is the position of the input a
#   in_program[i+2] is the position of the input b
#   in_program[i+3] is the position of the output


class IntCodeComputer:

    def __init__(self, input_string):
        self.program = input_string

    def run(self, user_input):
        i = 0
        diag_codes = list()
        input_counter = 0
        while True:
            opcode = self.program[i] % 100  # Last 2 digits
            param_modes = self.program[i] // 100  # first n-2 digits
            param_mode_a = param_modes % 10
            param_mode_b = (param_modes // 10) % 10
            # param_mode_c = (param_modes // 100) % 10
            if opcode == 1:  # add
                if param_mode_a == 1:
                    param_a = self.program[i + 1]
                else:
                    param_a = self.program[self.program[i + 1]]

                if param_mode_b == 1:
                    param_b = self.program[i + 2]
                else:
                    param_b = self.program[self.program[i + 2]]
                self.program[self.program[i + 3]] = param_a + param_b
                i += 4

            elif opcode == 2:  # multiply
                if param_mode_a == 1:
                    param_a = self.program[i + 1]
                else:
                    param_a = self.program[self.program[i + 1]]

                if param_mode_b == 1:
                    param_b = self.program[i + 2]
                else:
                    param_b = self.program[self.program[i + 2]]
                self.program[self.program[i + 3]] = param_a * param_b
                i += 4

            elif opcode == 3:  # take input
                self.program[self.program[i + 1]] = user_input[input_counter]
                # self.program[self.program[i + 1]] = int(input('please provide input'))
                input_counter += 1
                i += 2

            elif opcode == 4:  # output
                diag_codes.append(self.program[self.program[i + 1]])
                # print("diag code: ", self.program[self.program[i + 1]])
                i += 2

            elif opcode == 5:  # jump if true
                if param_mode_a == 1:
                    param_a = self.program[i + 1]
                else:
                    param_a = self.program[self.program[i + 1]]
                if param_mode_b == 1:
                    param_b = self.program[i + 2]
                else:
                    param_b = self.program[self.program[i + 2]]
                if param_a != 0:
                    i = param_b
                else:
                    i += 3

            elif opcode == 6:  # jump if false
                if param_mode_a == 1:
                    param_a = self.program[i + 1]
                else:
                    param_a = self.program[self.program[i + 1]]
                if param_mode_b == 1:
                    param_b = self.program[i + 2]
                else:
                    param_b = self.program[self.program[i + 2]]
                if param_a == 0:
                    i = param_b
                else:
                    i += 3

            elif opcode == 7:  # less than
                if param_mode_a == 1:
                    param_a = self.program[i + 1]
                else:
                    param_a = self.program[self.program[i + 1]]
                if param_mode_b == 1:
                    param_b = self.program[i + 2]
                else:
                    param_b = self.program[self.program[i + 2]]
                param_c = self.program[i + 3]
                if param_a < param_b:
                    self.program[param_c] = 1
                else:
                    self.program[param_c] = 0
                i += 4

            elif opcode == 8:  # Equals
                if param_mode_a == 1:
                    param_a = self.program[i + 1]
                else:
                    param_a = self.program[self.program[i + 1]]
                if param_mode_b == 1:
                    param_b = self.program[i + 2]
                else:
                    param_b = self.program[self.program[i + 2]]
                param_c = self.program[i + 3]
                if param_a == param_b:
                    self.program[param_c] = 1
                else:
                    self.program[param_c] = 0
                i += 4

            elif opcode == 99:  # end
                return self.program, diag_codes[-1]
            else:
                print("something went wrong")
                return -1
