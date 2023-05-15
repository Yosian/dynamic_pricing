# Josian Quintana-Arroyo, 15 May 23

import numpy as np


class DynamicPricingModel:
    def __init__(self, base_price, total_tickets):
        self.base_price = base_price
        self.total_tickets = total_tickets
        self.time_left = 1.0  # we'll represent this as a fraction, where 1.0 means 100% of the time is left
        self.tickets_left = total_tickets
        self.demand_rate = 1.0  # again, a fraction where 1.0 means normal demand

    def update(self, time_left, tickets_sold, demand_rate):
        self.time_left = time_left
        self.tickets_left = self.total_tickets - tickets_sold
        self.demand_rate = demand_rate

    def get_price(self):
        time_multiplier = np.sqrt(1.0 / self.time_left)  # price increases as time left decreases
        ticket_multiplier = np.sqrt(1.0 / (self.tickets_left / self.total_tickets))  # price increases as tickets left decreases
        demand_multiplier = self.demand_rate  # price increases as demand increases

        return self.base_price * time_multiplier * ticket_multiplier * demand_multiplier
