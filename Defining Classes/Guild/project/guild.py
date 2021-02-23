from project.player import Player


class Guild:
    def __init__(self, name: str, list_of_players=[]):
        self.name = name
        self.list_of_players = list_of_players

    def assign_player(self, player: Player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        else:
            self.list_of_players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        player = [p for p in self.list_of_players if p.name == player_name]
        if player:
            player[0].guild = "Unaffiliated"
            self.list_of_players.remove(player[0])
            return f"Player {player_name} has been removed from the guild."
        else:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for player in self.list_of_players:
            result += player.player_info()
        return result


# UNCOMMENT FOR TESTING PURPOSES
player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
