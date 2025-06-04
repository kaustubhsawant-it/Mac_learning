#Your code goes here. You modify the player() function here.

def player(prev_play,opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    
    if not opponent_history:
        return 'R'

    #Frequency analysis
    most_common = max(set(opponent_history), key=opponent_history.count)

    #Counter the most common moves
    counter_moves= {'R':'P','P':'S','S':'R'}
    return counter_moves[most_common]

