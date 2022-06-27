class Team():
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach 
        self.points = 0


    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player):
        for each_player in self.players:
            if player == each_player:
                return True
        return False

    def play_game(self, win):
        if win: self.points += 3 
        else: pass

        
