from enum import Enum


class RiskLevel(Enum):
    LOW = 0
    MID = 1
    HIGH = 2

class DataInterface:
    def get_items(self):
        raise NotImplementedError

    def get_hosts(self):
        raise NotImplementedError

    def get_item_count(self):
        raise NotImplementedError

    def get_high_probability_count(self):
        raise NotImplementedError

    def get_medium_probability_count(self):
        raise NotImplementedError

    def get_low_probability_count(self):
        raise NotImplementedError