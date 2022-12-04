# This solution was created by chat.openai.com. OpenAI Assistant. (2022, December 4)

# Prompts put in, separated by empty lines:

# read in input.txt which has lines such as '4-5,3-8'
# these represent pairs of ranges of integers, the first range is 4-5 and the second range is 3-8.
# find how many pairs have one range fully containing the other range
# then find how many pairs have overlapping ranges

#  add reading an input file called 'input.txt'

# ValueError: too many values to unpack (expected 2)
# line 11

# i think the problem is newline characters
#       context: pairs was like ['82-82', '8-83\n6-98', '6-93\n56-77']

# the input should be split on newlines before split on commas

# but it also needs to split each line into the two pairs

# for example there are two containing pairs and 4 overlapping pairs in this input:
# 2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8

# overlapping ranges:2
#       context: the example was getting the wrong result - the answer to this added int() because previously it was
#       comparing strings

# i don't think overlapping checks both ways round
#       this didn't result in a change

# there can't be more containing pairs than overlapping pairs - all pairs that contain each other must also overlap
#       this added more lines of logic and the result gave the right answers

# Final solution given:

# open input file
with open('input.txt', 'r') as f:
    # read and strip whitespace from file
    input_string = f.read().strip()

    # split input string on newlines to get individual pairs of ranges
    pairs = input_string.splitlines()

    # count for fully contained and overlapping ranges
    fully_contained = 0
    overlapping = 0

    # loop through each line of the input file
    for line in pairs:
        # split line on comma to get the two pairs of ranges
        r1, r2 = line.split(',')

        # split each pair on first dash to get start and end points of each range
        r1_start, r1_end = r1.split('-', 1)
        r2_start, r2_end = r2.split('-', 1)

        # convert range points to integers
        r1_start = int(r1_start)
        r1_end = int(r1_end)
        r2_start = int(r2_start)
        r2_end = int(r2_end)

        # check if one range fully contains the other
        if r1_start <= r2_start and r1_end >= r2_end:
            # check if ranges overlap
            if r1_start <= r2_end and r1_end >= r2_start:
                fully_contained += 1
                overlapping += 1
        elif r2_start <= r1_start and r2_end >= r1_end:
            # check if ranges overlap
            if r1_start <= r2_end and r1_end >= r2_start:
                fully_contained += 1
                overlapping += 1
        # check if ranges overlap
        elif r1_start <= r2_end and r1_end >= r2_start:
            overlapping += 1

    # print results
    print(f"Fully contained ranges: {fully_contained}")
    print(f"Overlapping ranges: {overlapping}")
