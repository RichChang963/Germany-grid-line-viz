import pandas as pd
from scripts.plot import plot_map

if __name__ == "__main__":
    data = pd.DataFrame({
        "year": [2020, 2021,2022],
        "load": [100,200,300],
        "latitude": [54, 52, 50],
        "longitude": [15, 8, 6]
    })
    plot_map(data=data)

    