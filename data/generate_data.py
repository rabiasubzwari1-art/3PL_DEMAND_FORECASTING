import pandas as pd
import numpy as np
from datetime import datetime

print("🚀 Generating demand data...")

# Configuration
START_DATE = "2019-01-01"
END_DATE = "2024-12-31"
NUM_HUBS = 5
OUTPUT_FILE = "data/logistics_demand.csv"

np.random.seed(42)

# Create date range
dates = pd.date_range(start=START_DATE, end=END_DATE, freq="D")

records = []

for hub_id in range(1, NUM_HUBS + 1):
    base_demand = np.random.randint(800, 1400)

    for date in dates:
        is_weekend = int(date.weekday() >= 5)
        is_festival = int(np.random.rand() < 0.08)

        fuel_price = round(np.random.normal(95, 6), 2)
        active_clients = np.random.randint(70, 160)
        orders = np.random.poisson(base_demand)

        demand = int(
            orders
            + active_clients * 2
            - fuel_price * 1.5
            + is_weekend * 120
            + is_festival * 200
            + np.random.normal(0, 50)
        )

        records.append([
            date,
            hub_id,
            orders,
            active_clients,
            fuel_price,
            is_weekend,
            is_festival,
            max(demand, 0)
        ])

columns = [
    "date",
    "hub_id",
    "orders",
    "active_clients",
    "fuel_price",
    "is_weekend",
    "is_festival",
    "demand"
]

df = pd.DataFrame(records, columns=columns)

df.to_csv(OUTPUT_FILE, index=False)

print("✅ Data generated successfully!")
print("📊 Total rows:", len(df))
print(df.head())

