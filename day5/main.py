lines = ['    [D]    ', '[N] [C]    ','[Z] [M] [P]']

def create_stack(lines:str):
    # Each stack takes 3 chars + 1 space = 4, to determine the number of stacks read 3 chars at a time
    stacks = []
    
    for j, line in enumerate(reversed(lines)):
        # print(f"number of elements = {(len(line)+1)/4}")
        for i in range(0, len(line), 4):
            # print(f"{i}, {i+3}")
            if j==0:
                stacks.append([])

            stack_id = int(i/4)
            # print(f"stack_id = {stack_id}")
            element = line[i+1:i+2].strip(" ")
            if element != "":
                stacks[stack_id].append(element)
            #    print(f"{line[i+1:i+2]}")
    # print(stacks)
    # print(f"Popping from First Stack -{stacks[0].pop()}")
    return stacks

def do_move(stacks:list, container_count:int, from_id:int, to_id:int):
    from_index = from_id - 1 
    to_index = to_id - 1

    for i in range(container_count):
        container = stacks[from_index].pop()
        stacks[to_index].append(container)
    
    return stacks

def do_multiple_move(stacks:list, container_count:int, from_id:int, to_id:int):
    # with multiple moves, simply add and slice the stacks
    from_index = from_id - 1 
    to_index = to_id - 1
    
    stack_slice = stacks[from_index][-container_count:]
    # print(f"stack_slice = {stack_slice}")
    stacks[to_index] = stacks[to_index] + stack_slice
    stacks[from_index] = stacks[from_index][:-container_count]
    # print(f"stacks={stacks}")    
    return stacks


def part1():
    with open("input.txt","r") as in_f:
        stack_lines = []
        section = "stacks"
        stacks = []
        for line in in_f:
            line = line.strip("\n")
            if line.startswith(" 1"):
                section = "move"
                stacks = create_stack(stack_lines)
                print(stacks)

            if section == "stacks":
                stack_lines.append(line)

            if line.startswith("move"):
                strs = line.split(" ")
                container_count = int(strs[1])
                from_id = int(strs[3])
                to_id = int(strs[5])
                # print(f"move - {container_count}")
                # stacks = do_move(stacks, container_count, from_id, to_id)
                stacks = do_multiple_move(stacks, container_count, from_id, to_id)

    # print(stacks)
    # Print the last element of each stack
    answer = ''
    for s in stacks:
        answer = answer+s[-1]
    print(answer)



if __name__ == "__main__":
    part1()