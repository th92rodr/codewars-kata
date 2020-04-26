
def dir_reduction(directions):
    opposites = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'WEST': 'EAST', 'EAST': 'WEST'}

    i = 0
    while i < len(directions) - 1:
        if directions[i+1] == opposites[directions[i]]:
            # opposites directions
            # remove both from the list and go back to the start of the list
            directions.pop(i+1)
            directions.pop(i)
            #del directions[i:i+2]
            i = 0

        else:
            # not opposites directions
            # keep on to the next position of the list
            i += 1

    return directions


print('North, South, South, East, West, North, West -> ', dir_reduction(['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']))

print('North, South, East, West -> ', dir_reduction(['NORTH', 'SOUTH', 'EAST', 'WEST']))

print('North, East, West, South, West, West -> ', dir_reduction(['NORTH', 'EAST', 'WEST', 'SOUTH', 'WEST', 'WEST']))
