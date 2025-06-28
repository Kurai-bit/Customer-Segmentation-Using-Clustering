import numpy as np
import pandas as pd
import h5py

n_customers = 50000
np.random.seed(0)

customer_ids = np.arange(1, n_customers + 1)
recency = np.random.randint(1, 365, size=n_customers)
frequency = np.random.poisson(lam=5, size=n_customers)
monetary = np.random.gamma(2, 100, n_customers)

with h5py.File("customer_segmentation.h5", "w") as f:
    f.create_dataset("customer_id", data=customer_ids)
    f.create_dataset("recency", data=recency)
    f.create_dataset("frequency", data=frequency)
    f.create_dataset("monetary", data=monetary)
