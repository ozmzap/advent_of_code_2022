score = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def part1():
    with open("input.txt","r") as in_f:
        final_score = 0
        for line in in_f:
            line = line.strip("\n")
            if line != "":
                # split line into 2 equal parts
                # print(f"Processing line - {line}")
                # print(f"length: {len(line)/2}")
                mid_point = int(len(line)/2)
                # Lets convert it into set to get unique values only
                s1 = set(line[:mid_point])
                s2 = set(line[mid_point:])
                common_objs = []
                for i in s1:
                    for j in s2:
                        if  i == j:
                            common_objs.append(i)
                            break
                # print(common_objs)

                for i in common_objs:
                    # print(f"Finding - {i}")
                    final_score = final_score + (score.index(i)+1)
        print(f"final_score = {final_score}")

def part2():
    # Read 3 lines at a time:
    with open("input.txt","r") as in_f:
        final_score = 0
        for i, line in enumerate(in_f):
            line = line.strip("\n")
            if i % 3 == 0:
                # Start a new group here
                s1 = set(line)
                s2 = None
                s3 = None
            if i % 3 == 1:
                 s2 = set(line)
            if i % 3 == 2:
                 s3 = set(line)
            if s1 is not None and s2 is not None and s3 is not None:
                for i in s1:
                    for j in s2:
                        if i==j:
                            for k in s3:
                                if i==k:
                                    final_score = final_score + score.index(i) + 1
    
    print(f"final_score = {final_score}")                               


if __name__ == "__main__":
    part2()