import pandas as pd
import os


def load_dataset():
    """
    Load EV dataset from CSV file.
    """

    # Get project root directory
    base_dir = os.path.dirname(os.path.dirname(__file__))

    # Build correct dataset path
    file_path = os.path.join(base_dir, "data", "ev_data.csv")

    data = pd.read_csv(file_path)
    return data


def calculate_energy_per_km(data):
    """
    Energy_per_km = Consumption / Distance
    """
    data["Energy_per_km"] = data["Consumption"] / data["Distance"]
    return data


def calculate_efficiency(data):
    """
    Efficiency = Distance / Consumption
    """
    data["Efficiency"] = data["Distance"] / data["Consumption"]
    return data


def energy_analysis():
    """
    Perform full energy analysis
    """

    data = load_dataset()

    data = calculate_energy_per_km(data)
    data = calculate_efficiency(data)

    avg_energy = data["Energy_per_km"].mean()
    avg_efficiency = data["Efficiency"].mean()

    print("Average Energy per km:", round(avg_energy, 3))
    print("Average Efficiency (km per unit energy):", round(avg_efficiency, 3))

    return data


if __name__ == "__main__":
    energy_analysis()
