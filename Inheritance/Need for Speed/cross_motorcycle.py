from project.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):
    def __init__(self, fuel, horse_power):
        Motorcycle.__init__(self, fuel, horse_power)