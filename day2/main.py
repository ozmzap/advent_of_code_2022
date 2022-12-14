from datetime import datetime
'''
A, X - Rock - 1 points
B, Y - Paper - 2 points
C, Z - Scissor - 3 points
X - Loss = 0 points
Y - Draw = 3 points
Z - Win = 6 points
rock defeats scissor
scissor defeats paper
paper defeats rock
'''
class RPSGame:
    
    def __init__(self):
        self._me = None
        self._opponent = None
        self._outcome = None
        self.__play_points = 0
        self.__outcome_points = 0
        self.__pp_map = {"rock":1, "paper":2, "scissor":3}
    
    @property
    def me(self):
        return self._me

    @me.setter
    def me(self, value):
        self._me = value
        # Set play points
        self.__play_points = self.__pp_map[value]
        if self._opponent is not None:
            self.__calculate_outcome()
    
    @property
    def opponent(self):
        return self._opponent

    @opponent.setter
    def opponent(self, value):
        self._opponent = value
        if self._me is not None:
            self.__calculate_outcome()
    
    @property
    def outcome(self):
        return self._outcome
    
    @outcome.setter
    def outcome(self, value):
        self._outcome = value
        if self._opponent is not None:
            self.__calculate_my_play()

    def __calculate_my_play(self):
        if self._outcome == "draw":
            # Draw
            self.__outcome_points = 3
            self._me = self._opponent
            self.__play_points = self.__pp_map[self._me]
        elif self._outcome == "win":
            # Win
            self.__outcome_points = 6
            if self._opponent == "scissor":
                self._me = "rock"
            if self._opponent == "paper":
                self._me = "scissor"
            if self._opponent == "rock":
                self._me = "paper"
            self.__play_points = self.__pp_map[self._me]
        else:
            # Loss
            self.__outcome_points = 0
            if self._opponent == "scissor":
                self._me = "paper"
            if self._opponent == "paper":
                self._me = "rock"
            if self._opponent == "rock":
                self._me = "scissor"
            self.__play_points = self.__pp_map[self._me]

    def __calculate_outcome(self):
        if self._me == self._opponent:
            # draw
            self._outcome = "draw"
            self.__outcome_points = 3
        elif ((self._me == "rock" and self._opponent == "scissor")
        or (self._me == "scissor" and self._opponent == "paper")
        or (self._me == "paper" and self._opponent == "rock")):
            # Win
            self._outcome = "win"
            self.__outcome_points = 6
        else:
            # Loss
            self._outcome = "loss"
            self.__outcome_points = 0
        # print(f"Outcome Points = {self.__outcome_points}, {self._outcome}")

    def get_points(self) -> int:
        # print(f"{self.__play_points}, {self.__outcome_points}")
        return self.__play_points + self.__outcome_points
    
RPS_MAP = {"A":"rock","B":"paper","C":"scissor"}
XYZ_OUTCOME_MAP = {"X":"loss","Y":"draw","Z":"win"}
XYZ_RPS_MAP = {"X":"rock","Y":"paper","Z":"scissor"}

def calculate_points(opponent: str, mine: str):
    if opponent == "rock" and mine == "rock":
        # Draw
        return 1 + 3
    elif opponent == "rock" and mine == "paper":
        # Win
        return 2 + 6
    elif opponent == "rock" and mine == "scissor":
        # Loss
        return 0 + 3
    elif opponent == "paper" and mine == "paper":
        # Draw
        return 2 + 3 
    elif opponent == "paper" and mine == "rock":
        # Loss
        return 0 + 1
    elif opponent == "paper" and mine == "scissor":
        # Win
        return 6 + 3    
    elif opponent == "scissor" and mine == "scissor":
        # Draw
        return 3 + 3
    elif opponent == "scissor" and mine == "rock":
        # Win
        return 6 + 1
    elif opponent == "scissor" and mine == "paper":
        # Loss
        return 0 + 2
    else:
        return 0

def get_points_from_plays(opponent, mine):
    rps_game = RPSGame()
    rps_game.opponent = RPS_MAP[opponent]
    rps_game.me = XYZ_RPS_MAP[mine]
    return rps_game.get_points()

def get_points_from_outcome(opponent, outcome):
    rps_game = RPSGame()
    rps_game.opponent = RPS_MAP[opponent]
    rps_game.outcome = XYZ_OUTCOME_MAP[outcome]
    return rps_game.get_points()

def do_main(use:str):
    print(f"Starting function @{datetime.now()}")
    # with open("input.txt", "r") as in_f, open("output_method2.txt","w") as out_f:
    with open("input.txt", "r") as in_f:
        final_score = 0
        for line in in_f:
            line = line.strip("\n")
            plays = line.split(" ")
            abc = plays[0]
            xyz = plays[1]
            # Calculate outcome when opponent and my play is known
            if use == "play":
                final_score = final_score + get_points_from_plays(abc, xyz)
            if use == "outcome":
                final_score = final_score + get_points_from_outcome(abc, xyz)
            
            # out_f.write(f"{opponent},{mine},{calculate_points(RPS_MAP[opponent], XYZ_RPS_MAP[mine])}\n")
            # final_score = final_score + calculate_points(RPS_MAP[opponent], XYZ_RPS_MAP[mine])
            
    print(f"Final Score: {final_score}")
    print(f"Ending function @{datetime.now()}")
if __name__ == "__main__":
    # do_main("play")
    do_main("outcome")