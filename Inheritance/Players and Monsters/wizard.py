from project.hero import Hero


class Wizard(Hero):
    def __init__(self, name, level):
        Hero.__init__(self,name,level)