#Has the play() function and built-in bots like quincy, abbey, kris, and mrugesh. Don’t change this file.

import random

def play(player1,player2,num_games=10, verbose=False):
    p1_history=[]
    p2_history=[]

    p1_score=0
    p2_score=0

    for game in range(num_games):
        prev_p1 = p1_history[-1] if p1_history else ""
        prev_p2 = p2_history[-1] if p2_history else ""

        p1_move = player1(prev_p1)
        p2_move = player2(prev_p2)

        p1_history.append(p1_move)
        p2_history.append(p2_move)

        if verbose:
            print(f"Game {game+1}:")
            print(f"Player 1: {p1_move}, Player 2: {p2_move}")

        if p1_move == p2_move:
            if verbose:
                print("Tie\n")
        elif ((p1_move =="R" and p2_move =="S") or (p1_move=="S" and p2_move=="P") or (p1_move=="P" and p2_move=="R")):
            p1_score+=1
            if verbose:
                print("Player 1 wins\n")
        else:
            p2_score+=1
            if verbose:
                print("Player 2 wins\n")

    print(f"\nFinal score after {num_games} games:")
    print(f"Player 1: {p1_score}")
    print(f"Player 2: {p2_score}")

    if p1_score > p2_score:
        print("Player 1 wins the match!")
    elif p2_score > p1_score:
        print("Player 2 wins the match!")
    else:
        print("It is a tie!")

def quincy(prev_play):
    return "P"

def abbey(prev_play, abbey_history=[]):
    if prev_play:
        abbey_history.append(prev_play)

    if (len(abbey_history) < 3):
        return "R"
    else:
        return abbey_history[-3]
    
def kris(prev_play):
    return "S"

def mrugesh(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    
    if (len(opponent_history) < 2):
        return "R"
    
    return random.choice(["R","P","S"])

