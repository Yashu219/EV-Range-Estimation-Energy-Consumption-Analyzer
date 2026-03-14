import pandas as pd


def load_dataset(file_path="data/ev_data.csv"):
    """
    Load EV dataset from CSV file.
    
    Parameters:
    file_path (str): Path to the dataset
    
    Returns:
    pandas.DataFrame
    """
    data = pd.read_csv(file_path)
    return data


def calculate_energy_per_km(data):
    """
    Calculate energy consumed per kilometer.
    
    Energy_per_km = Consumption / Distance
    """
    data["Energy_per_km"] = data["Consumption"] / data["Distance"]
    return data


def calculate_efficiency(data):
    """
    Calculate EV efficiency (km per unit energy).
    
    Efficiency = Distance / Consumption
    """
    data["Efficiency"] = data["Distance"] / data["Consumption"]
    return data


def energy_analysis(file_path="ev_data.csv"):
    """
    Perform full energy analysis on EV dataset.
    """
    
    # Load data
    data = load_dataset(file_path)

    # Calculate metrics
    data = calculate_energy_per_km(data)
    data = calculate_efficiency(data)

    # Summary statistics
    avg_energy = data["Energy_per_km"].mean()
    avg_efficiency = data["Efficiency"].mean()

    print("Average Energy per km:", round(avg_energy, 3))
    print("Average Efficiency (km per unit energy):", round(avg_efficiency, 3))

    return data


if __name__ == "__main__":
    energy_analysis()
