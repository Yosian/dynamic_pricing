import pytest
import numpy as np
from model.repository import DynamicPricingModel


class TestDynamicPricingModel:

    @pytest.fixture
    def model(self):
        return DynamicPricingModel(base_price=100.0, total_tickets=1000)

    def test_initial_price(self, model):
        assert model.get_price() == 100.0

    def test_time_update(self, model):
        model.update(time_left=0.5, tickets_sold=0, demand_rate=1.0)
        assert model.get_price() == 100.0 * np.sqrt(2)

    def test_ticket_update(self, model):
        model.update(time_left=1.0, tickets_sold=500, demand_rate=1.0)
        assert model.get_price() == 100.0 * np.sqrt(2)

    def test_demand_update(self, model):
        model.update(time_left=1.0, tickets_sold=0, demand_rate=1.5)
        assert model.get_price() == 100.0 * 1.5

    def test_all_factors_update(self, model):
        model.update(time_left=0.5, tickets_sold=500, demand_rate=1.5)
        assert model.get_price() == 100.0 * np.sqrt(2) * np.sqrt(2) * 1.5
