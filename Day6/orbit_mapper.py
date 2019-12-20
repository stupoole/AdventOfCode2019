with open("input_orbits.txt") as f:
    in_orbits = f.readlines()


#  makes a dictionary of orbits[orbiting body] = center of orbit or orbits[child] = parent
orbits = dict()
for orbit in in_orbits:
    parent, child = orbit.rstrip().split(')')
    orbits[child] = parent

#  Loops through each body and steps back through each body counting how many steps it takes to reach the common.
orbit_count = 0
for child in orbits:
    orbit_count += 1
    parent = orbits[child]
    while parent in orbits.keys():
        parent = orbits[parent]
        orbit_count += 1


root_count = 0
path_count = 0

# start point at yourself and iterate until find common meeting point
root = orbits["YOU"]
target = orbits["SAN"]
children = list()
while True:
    # step down into each branch and search the entire branch
    children = [k for k, v in orbits.items() if v == root]
    limit = True
    i = 0
    while limit:
        child = children[i]
        i += 1
        new_children = [k for k, v in orbits.items() if v == child]
        if new_children:
            children += new_children
        if i >= len(children):
            limit = False
    if target not in children:  # change the root to search further
        root = orbits[root]
        root_count += 1
    else:  # now change to santa
        break


# Start point at santa and count orbits to common meeting point
root = orbits["SAN"]
target = orbits["YOU"]
children = list()
while True:
    # step down into each branch and search the entire branch
    children = [k for k, v in orbits.items() if v == root]
    limit = True
    i = 0
    while limit:
        child = children[i]
        i += 1
        new_children = [k for k, v in orbits.items() if v == child]
        if new_children:
            children += new_children

        if i >= len(children):
            limit = False
    if target not in children:  # change the root to search further
        root = orbits[root]
        path_count += 1
    else:  # done
        break

print("part 1: ", orbit_count)
print("part 2: ", root_count + path_count)
