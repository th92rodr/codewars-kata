'''
Directions Reduction

Once upon a time, on a way through the old wild mountainous west, a man was given directions to go from one point to another.
The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.

Going to one direction and coming back the opposite direction right away is a needless effort.
Since this is the wild west, with dreadful weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!

How I crossed a mountainous desert the smart way.

The directions given to the man are, for example, the following:
["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]

You can immediately see that going "NORTH" and immediately "SOUTH" is not reasonable, better stay to the same place!
So the task is to give to the man a simplified version of the plan. A better plan in this case is simply:
["WEST"]


Other examples:
In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH" is going north and coming back right away.
The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other, therefore, the final result is [].

In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH" are not directly opposite but they become
directly opposite after the reduction of "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].


Task:
Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).


Notes:
Not all paths can be made simpler.
The path ["NORTH", "WEST", "SOUTH", "EAST"] is not reducible.
"NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" are not directly opposite of each other and can't become such.
Hence the result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].
'''

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
