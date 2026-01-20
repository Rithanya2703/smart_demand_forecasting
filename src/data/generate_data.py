import pandas as pd
import numpy as np

np.random.seed(42)

#parameters
start_date = '2023-01-01'
end_date = '2023-12-31'
dates = pd.date_range(start_date,end_date)

dishes = {'Briyani': 250, 'Dosa': 80,"Paneer Curry": 180,
    "Fried Rice": 150,
    "Soup": 120}

data = []

for date in dates:
    for dish, price in dishes.items():
        day_of_week = date.day_name()
        is_weekend = 1 if day_of_week in ["Saturday", "Sunday"] else 0
        is_holiday = np.random.choice([0,1], p=[0.9,0.1])
        promotion = np.random.choice([0,1], p=[0.85, 0.15])

        temperature = np.random.normal(30, 5)
        rainfall = max(0, np.random.normal(3,5))
    
        base_demand = 40
        if dish == 'Briyani':
            base_demand += 30
        if dish == "Soup" and temperature < 25:
            base_demand += 35

        orders = (
            base_demand
            + is_weekend * 10
            + promotion * 15
            + is_holiday *20
            - price * 0.05
            + np.random.normal(0,5)
        )

        orders = max(0, int(orders))

        data.append ({
            'date': date,
            'dish': dish,
            'price': price, 
            'orders': orders,
            'is_weekend': is_weekend,
            'is_holiday': is_holiday,
            'promotion': promotion,
            'temperature': round(temperature,2),
            'rainfall': round(rainfall,2)
        })

        df = pd.DataFrame(data,columns=columns)
        df.to_csv('smart_demand_forecasting/data/smart_demand_data.csv', index=False)
print("Data generation complete. Dataset saved to 'smart_demand_forecasting/data/smart_demand_data.csv'", df.shape)

