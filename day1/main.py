'''
elves: list of calories of each elf
Read lines from file
Do sum till you encounter a blank
Append calculated value in elves list
Reset sum counter
Find index of max value and max value from elves list
'''
def do_main():
    with open("input.txt", "r") as in_f:
        elves = []
        elf_calories = 0 
        for line in in_f:
            line = line.strip("\n")
            
            if line == "":
                elves.append(elf_calories)
                elf_calories = 0
            else:
                elf_calories = elf_calories + int(line)

    # max_index = 0
    # max_value = 0
    # for i, v in enumerate(elves):
    #     if v > max_value:
    #         max_value = v
    #         max_index = i
    
    # print(f"Elf {max_index} has the most calories - {max_value}")

    # We need the top 3 elves now, best to sort the list in descending order
    elves.sort(reverse=True)
    result = elves[0] + elves[1] + elves[2]
    print(f"Top 3 elsves - {result}")

if __name__ == "__main__":
    do_main()