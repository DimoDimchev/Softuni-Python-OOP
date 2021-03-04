class Zoo:
    def __init__(self, name, budget, animlal_capacity, workers_capacity):
        self.name = name
        self.animals = []
        self.workers = []
        self.__animal_capacity = animlal_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget

    def add_animal(self, animal, price):
        if self.__animal_capacity > 0:
            if self.__budget >= price:
                self.__animal_capacity -= 1
                self.__budget -= price
                self.animals.append(animal)
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > 0:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        worker = [worker for worker in self.workers if worker.name == worker_name]
        if worker:
            worker = worker[0]
            self.workers.remove(worker)
            self.__workers_capacity += 1
            return f"{worker.name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = sum([worker.salary for worker in self.workers])
        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        costs = sum([animal.get_needs() for animal in self.animals])
        if self.__budget >= costs:
            self.__budget -= costs
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [lion for lion in self.animals if lion.get_needs() == 50]
        tigers = [tiger for tiger in self.animals if tiger.get_needs() == 45]
        cheetahs = [cheetah for cheetah in self.animals if cheetah.get_needs() == 60]

        result = ""
        result += f"You have {len(self.animals)} animals\n----- {len(lions)} Lions:\n"
        result += '\n'.join([lion.__repr__() for lion in lions]) + '\n'
        result += f"----- {len(tigers)} Tigers:\n"
        result += '\n'.join([tiger.__repr__() for tiger in tigers]) + '\n'
        result += f"----- {len(tigers)} Cheetahs:\n"
        result += '\n'.join([cheetah.__repr__() for cheetah in cheetahs])

        return result

    def workers_status(self):
        keepers = [keeper for keeper in self.workers if keeper.__class__.__name__ == "Keeper"]
        caretakers = [caretaker for caretaker in self.workers if caretaker.__class__.__name__ == "Caretaker"]
        vets = [vet for vet in self.workers if vet.__class__.__name__ == "Vet"]

        result = f"You have {len(self.workers)} workers\n"
        result += f"----- {len(keepers)} Keepers:\n"
        result += '\n'.join([k.__repr__() for k in keepers]) + '\n'
        result += f"----- {len(caretakers)} Caretakers:\n"
        result += '\n'.join([c.__repr__() for c in caretakers]) + '\n'
        result += f"----- {len(vets)} Vets:\n"
        result += '\n'.join([v.__repr__() for v in vets])

        return result
