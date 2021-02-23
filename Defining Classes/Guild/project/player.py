class Player:
    def __init__(self, name: str, hp: int, mp: int, skills={}, guild="Unaffiliated"):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = skills
        self.guild = guild

    def add_skill(self, skill_name: str, mana_cost: int):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        else:
            return "Skill already added"

    def player_info(self):
        data = f'Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n'
        for skill, cost in self.skills.items():
            data += f"==={skill} - {cost}\n"
        return data
