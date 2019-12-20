input_range = range(245182, 790572)


#  Returns true if there is atleast a double and the digits are counting up or the same.
def filter_part1(in_string):
    a, b, c, d, e, f = in_string
    a, b, c, d, e, f = int(a), int(b), int(c), int(d), int(e), int(f)
    ordering = f >= e >= d >= c >= b >= a
    doubles = a == b or b == c or c == d or d == e or e == f

    return ordering and doubles


#  Returns true if there is atleast 1 double and not triple, and counts up.
def filter_part2(in_string):
    a, b, c, d, e, f = in_string
    a, b, c, d, e, f = int(a), int(b), int(c), int(d), int(e), int(f)
    ordering = f >= e >= d >= c >= b >= a
    doubles = sum([a == b and a != c, b == c and c != d and a != b, c == d and c != e and c != b,
                   d == e and d != f and d != c, e == f and e != d]) >= 1
    # print(doubles)

    return ordering and doubles


input_strings = (str(a) for a in input_range)
filtered_1 = tuple(filter(filter_part1, input_strings))
input_strings = (str(a) for a in input_range)
filtered_2 = tuple(filter(filter_part2, input_strings))

print("part1: ", len(filtered_1))
print("part2: ", len(filtered_2))
