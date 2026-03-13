import pandas as pd

def load_dataset():
    data = pd.read_csv("ev_data.csv")
    return data

def calculate_energy_per_km(data):
    data["Energy_per_km"] = data["Consumption"] / data["Distance"]
    return data

def calculate_efficiency(data):
    data["Efficiency"] = data["Distance"] / data["Consumption"]
    return data

def energy_analysis():
    data = load_dataset()

    data = calculate_energy_per_km(data)
    data = calculate_efficiency(data)

    print(data.head())

    return data
