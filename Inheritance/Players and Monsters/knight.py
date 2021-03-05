from project.hero import Hero


class Knight(Hero):
    def __init__(self, name, level):
        Hero.__init__(self,name,level)