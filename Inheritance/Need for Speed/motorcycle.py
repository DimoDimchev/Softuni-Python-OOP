from project.vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, fuel, horse_power):
        Vehicle.__init__(self, fuel, horse_power)
