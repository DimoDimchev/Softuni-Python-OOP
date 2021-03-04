class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    @property
    def name(self):
        return self.__name

    @property
    def rating(self):
        return self.__rating

    @property
    def players(self):
        return self.__players

    @name.setter
    def name(self, new_value):
        self.__name = new_value

    @rating.setter
    def rating(self, new_value):
        self.__rating = new_value

    @players.setter
    def players(self, new_value):
        self.players = new_value

    def add_player(self, player):
        if player not in self.__players:
            self.__players.append(player)
            return f"Player {player.name} joined team {self.__name}"
        return f"Player {player.name} has already joined"

    def remove_player(self, player_name):
        player = [player for player in self.__players if player.name == player_name]
        if player:
            player = player[0]
            self.__players.remove(player)
            return player
        return f"Player {player_name} not found"