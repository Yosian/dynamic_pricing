from model.repository import DynamicPricingModel

model = DynamicPricingModel(base_price=100.0, total_tickets=1000)

# Update the model based on the current state of the event
model.update(time_left=0.1, tickets_sold=700, demand_rate=2.2)
model.get_price()