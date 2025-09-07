import math
from dataclasses import dataclass


@dataclass
class EOQInputs:
    demand: float  # annual demand (units)
    ordering_cost: float  # per order cost ($)
    holding_rate: float  # holding cost rate (e.g., 0.2 for 20%/year)
    unit_cost: float  # cost per unit ($)
    lead_time_days: int  # supplier lead time
    demand_std_daily: float  # daily demand std dev
    service_z: float = 1.65  # ~95% cycle service level


def eoq(inputs: EOQInputs):
    h = inputs.holding_rate * inputs.unit_cost
    q = math.sqrt((2 * inputs.demand * inputs.ordering_cost) / h)
    return q


def reorder_point(
    avg_daily_demand: float, lead_time_days: int, demand_std_daily: float, service_z: float = 1.65
):
    safety = service_z * demand_std_daily * math.sqrt(lead_time_days)
    return avg_daily_demand * lead_time_days + safety


if __name__ == "__main__":
    sample = EOQInputs(
        demand=10000,
        ordering_cost=50,
        holding_rate=0.2,
        unit_cost=10,
        lead_time_days=14,
        demand_std_daily=5,
    )
    q = eoq(sample)
    rop = reorder_point(
        avg_daily_demand=10000 / 365,
        lead_time_days=sample.lead_time_days,
        demand_std_daily=sample.demand_std_daily,
    )
    print({"EOQ": round(q, 2), "ROP": round(rop, 2)})
