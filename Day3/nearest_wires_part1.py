import numpy as np

directions = {"R": np.array([[1, 0]]), "L": np.array([[-1, 0]]), "U": np.array([[0, 1]]), "D": np.array([[0, -1]])}


def draw_snake(input_string_):
    pos = np.array([[0, 0]])
    positions = np.empty(shape=(0, 2))
    for move in input_string_:
        direction = move[0]
        distance = int(move[1:])
        if (direction == "R") or (direction == "L"):
            spacesx = np.array([np.arange(pos[0, 0], pos[0, 0] + distance * directions[direction][0, 0],
                                          np.sign(directions[direction][0, 0] + 0.1))])
            spacesy = np.ones((1, distance)) * pos[0, 1]
        else:
            spacesx = np.ones((1, distance)) * pos[0, 0]
            spacesy = np.array([np.arange(pos[0, 1], pos[0, 1] + distance * directions[direction][0, 1],
                                          np.sign(directions[direction][0, 1] + 0.1))])
        pos += directions[direction] * (distance)

        positions = np.append(positions, np.vstack((spacesx, spacesy)).T, axis=0)

    return positions


file_token = open("input_wires.txt", "r")
in_wires = np.genfromtxt(file_token, delimiter=',', dtype='str')
file_token.close()

line1 = draw_snake(in_wires[0, :])[1:, :]
temp1, ind1 = np.unique(line1, return_index=True, axis=0)
set1 = set(map(tuple, line1))
tuple1 = tuple(map(tuple, line1))

line2 = draw_snake(in_wires[1, :])[1:, :]
temp2, ind2 = np.unique(line2, return_index=True, axis=0)
set2 = set(map(tuple, line2))
tuple2 = tuple(map(tuple, line2))
a = filter(lambda pos: pos in set2, set1)

crossings = set()
for pos in a:
    # print(pos)
    crossings.update([pos])

times = np.array([])
for crossing in crossings:
    # print(crossing, tuple1.index(crossing), tuple2.index(crossing))
    times = np.append(times, tuple1.index(crossing) + tuple2.index(crossing))

print("p1: ", min(abs(x) + abs(y) for x, y in crossings))
print("p2: ", sorted(times)[0])
