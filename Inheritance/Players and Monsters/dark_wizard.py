from project.wizard import Wizard


class DarkWizard(Wizard):
    def __init__(self, name, level):
        Wizard.__init__(self, name, level)