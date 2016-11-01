
colours = ['#','|','@']

colour_length = 1

pattern_length = 18

pattern_width = 4

print("Here is your scarf:\n")
for pos in range(int(pattern_width * pattern_length)):
    print colours[int((pos)/colour_length)%len(colours)]," ",
    if (pos % pattern_width) == pattern_width-1:
        print("")

