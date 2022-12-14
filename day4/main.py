
def part1():
    with open("input.txt","r") as in_f:
        count = 0
        for line in in_f:
            line = line.strip("\n")
            r1, r2 = line.split(",")[0], line.split(",")[1]
            r11, r12 = int(r1.split("-")[0]), int(r1.split("-")[1])
            r21, r22 = int(r2.split("-")[0]), int(r2.split("-")[1])
            
            if ((r11 >= r21 and r11 <= r22 and r12 >= r21 and r12 <= r22)
            or (r21 >= r11 and r21 <= r12 and r22 >= r11 and r22 <= r12)):
                count = count+1
        print(f"count={count}")

def part2():
    with open("input.txt","r") as in_f:
        count = 0
        for line in in_f:
            line = line.strip("\n")
            r1, r2 = line.split(",")[0], line.split(",")[1]
            r11, r12 = int(r1.split("-")[0]), int(r1.split("-")[1])
            r21, r22 = int(r2.split("-")[0]), int(r2.split("-")[1])
            
            if ((r11 >= r21 and r11 <= r22)
            or (r12 >= r21 and r12 <= r22)
            or (r21 >= r11 and r21 <= r12)
            or (r22 >= r11 and r22 <= r12)
            ):
                count = count+1
        print(f"count={count}")

if __name__ == "__main__":
    part2()