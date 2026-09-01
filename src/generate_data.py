import json
import random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(42)

OUTPUT_DIR = Path("data/raw")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

industries = [
    "Healthcare",
    "Manufacturing",
    "Retail",
    "Finance",
    "Technology",
]

regions = [
    "North",
    "South",
    "East",
    "West",
]

channels = [
    "Email",
    "Phone",
    "Web",
    "Chat",
]

interaction_types = [
    "Support",
    "Complaint",
    "Product Inquiry",
    "Sales",
]

products = [
    ("P001", "CRM Software", 1200),
    ("P002", "Analytics Platform", 1800),
    ("P003", "Cloud Services", 950),
    ("P004", "Data Integration", 1500),
    ("P005", "Customer Support", 700),
]


def generate_customers(n=1000):
    customers = []

    for i in range(1, n + 1):
        registration_date = datetime(2021, 1, 1) + timedelta(
            days=random.randint(0, 1800)
        )

        customers.append(
            {
                "customer_id": f"C{i:04d}",
                "customer_type": random.choice(
                    ["B2B", "B2C"]
                ),
                "industry": random.choice(industries),
                "region": random.choice(regions),
                "registration_date": registration_date.date().isoformat(),
                "annual_revenue": round(
                    random.uniform(10000, 500000), 2
                ),
                "customer_status": random.choice(
                    ["Active", "Active", "Active", "Inactive"]
                ),
            }
        )

    return customers


def generate_orders(customers, n=5000):
    orders = []

    start_date = datetime(2024, 1, 1)

    for i in range(1, n + 1):
        customer = random.choice(customers)
        product_id, _, price = random.choice(products)

        quantity = random.randint(1, 10)

        order_date = start_date + timedelta(
            days=random.randint(0, 970)
        )

        orders.append(
            {
                "order_id": f"O{i:06d}",
                "customer_id": customer["customer_id"],
                "order_date": order_date.date().isoformat(),
                "product_id": product_id,
                "quantity": quantity,
                "revenue": round(
                    quantity * price * random.uniform(0.8, 1.2),
                    2,
                ),
                "order_status": random.choice(
                    ["Completed", "Completed", "Completed", "Cancelled"]
                ),
            }
        )

    return orders


def generate_interactions(customers, n=3000):
    interactions = []

    start_date = datetime(2024, 1, 1)

    for i in range(1, n + 1):
        customer = random.choice(customers)

        interaction_date = start_date + timedelta(
            days=random.randint(0, 970)
        )

        interaction_type = random.choice(interaction_types)

        interactions.append(
            {
                "interaction_id": f"I{i:06d}",
                "customer_id": customer["customer_id"],
                "interaction_date": interaction_date.date().isoformat(),
                "channel": random.choice(channels),
                "interaction_type": interaction_type,
                "resolution_time_hours": round(
                    random.uniform(1, 72), 1
                ),
                "satisfaction_score": random.randint(1, 5),
            }
        )

    return interactions


def save_json(filename, data):
    with open(OUTPUT_DIR / filename, "w") as file:
        json.dump(data, file, indent=2)


if __name__ == "__main__":
    customers = generate_customers()
    orders = generate_orders(customers)
    interactions = generate_interactions(customers)

    save_json("customers.json", customers)
    save_json("orders.json", orders)
    save_json("interactions.json", interactions)

    print("CRM dataset generated successfully.")
    print(f"Customers: {len(customers)}")
    print(f"Orders: {len(orders)}")
    print(f"Interactions: {len(interactions)}")
