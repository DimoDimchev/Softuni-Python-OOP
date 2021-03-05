from project.reptile import Reptile


class Lizard(Reptile):
    def __init__(self, name):
        Reptile.__init__(self,name)