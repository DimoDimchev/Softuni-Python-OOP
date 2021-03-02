class Gym:
    def __init__(self):
        self.customers = []
        self.equipment = []
        self.trainers = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = [subscription for subscription in self.subscriptions if subscription.id == subscription_id][0]
        trainer = [trainer for trainer in self.trainers if trainer.id == subscription.trainer_id][0]
        customer = [customer for customer in self.customers if customer.id == subscription.customer_id][0]
        plan = [plan for plan in self.plans if plan.id == subscription.exercise_id][0]
        equipment = [equipment for equipment in self.equipment if equipment.id == plan.equipment_id][0]

        result = f"{subscription}\n{customer}\n{trainer}\n{equipment}\n{plan}"
        return result
