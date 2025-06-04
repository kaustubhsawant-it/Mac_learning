#Contains unit tests to check if your bot performs well. These are imported into main.py

from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player

def test_player_module():
    bots = [quincy, abbey, kris, mrugesh]
    names = ["quincy", "abbey", "kris", "mrugesh"]

    for bot,name in zip(bots,names):
        print(f"\nTesting against: {name}")
        result = play(player,bot,10)