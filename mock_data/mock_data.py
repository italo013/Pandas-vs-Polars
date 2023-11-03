import pandas as pd
import numpy as np
import random

sizes = [50000, 100000, 250000, 500000, 1000000, 2500000, 5000000]
categories = ['category1', 'category2']

for size in sizes:
    start_date = pd.to_datetime('2000-01-01')
    end_date = pd.to_datetime('2023-12-31')
    date_range = pd.date_range(start_date, end_date, periods=size)

    df = pd.DataFrame({
        'A': date_range,
        'B': np.random.rand(size),
        'C': np.random.randint(0, 100, size),
        'D': np.random.uniform(0.0, 1.0, size),
        'E': ['string' + str(i) for i in range(size)],
        'F': pd.Categorical([random.choice(categories) for _ in range(size)], ordered=True, categories=categories)
    })
    df.to_csv(f'mock_data_{size}.csv', index=False)
    if size <= 1000000: 
        df.to_excel(f'mock_data_{size}.xlsx', index=False)