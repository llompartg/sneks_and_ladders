import random

class cellinfo:
    def __init__(self, position, celltype):
        self.position = position
        self.celltype = celltype
        
class player:
    def __init__(self, name):
        self.name = name
        self.position = 0
        
class sneks_and_laders:
    def __init__(self, players):
        self.players = []
        for playerName in players:
            self.players.append(player(playerName))
        self.map = {
            '2': cellinfo(38, "ladder"),
            '7': cellinfo(14, "ladder"),
            '8': cellinfo(31, "ladder"),
            '15': cellinfo(26, "ladder"),
            '16': cellinfo(6, "snek"),
            '21': cellinfo(42, "ladder"),
            '28': cellinfo(84, "ladder"),
            '36': cellinfo(44, "ladder"),
            '46': cellinfo(25, "snek"),
            '49': cellinfo(11, "snek"),
            '51': cellinfo(67, "ladder"),
            '62': cellinfo(19, "snek"),
            '64': cellinfo(60, "snek"),
            '71': cellinfo(91, "ladder"),
            '74': cellinfo(53, "snek"),
            '78': cellinfo(98, "ladder"),
            '87': cellinfo(94, "ladder"),
            '89': cellinfo(68, "snek"),
            '92': cellinfo(88, "snek"),
            '95': cellinfo(75, "snek"),
            '99': cellinfo(80, "snek")
        }
            
    def play(self):
        while True:
            for player in self.players:
                print("It's", player.name, "'s turn")
                print(player.name, "is at position", str(player.position))
                rolled = random.randrange(6) + 1
                print(player.name, "rolled", str(rolled))
                player.position +=rolled
                if player.position > 100:
                    print (player.name, "bounces back from 100!")
                    player.position = 100 - (player.position - 100)
                print(player.name, "moves to position", str(player.position))
                if str(player.position) in self.map:
                    cell = self.map[str(player.position)]
                    if cell.celltype == "snek":
                        print("Woops!")
                    else:
                        print("Wow!")
                    print (player.name, "found a", cell.celltype, "!")
                    print(player.name, "moves to", cell.position,"!")
                    player.position = cell.position
                if player.position == 100:
                    print(player.name, "wins!")
                    self._end()
                    return
    def _end(self):
        print ("RESULTS!")
        for player in self.players:
            print (player.name, "position: ", player.position)
    
if __name__ == "__main__":
    players = [
        "Player1",
        "Player2"
    ]
    game = sneks_and_laders(players)
    game.play()
