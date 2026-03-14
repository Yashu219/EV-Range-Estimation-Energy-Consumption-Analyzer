from modules.range_calculation import run
from modules.energy_analysis import energy_analysis


def start_interface():
    print("EV Range Estimation & Energy Analyzer")
    print("-------------------------------------")

    battery = float(input("Enter Battery Capacity (kWh): "))
    soc = float(input("Enter State of Charge (%): "))

    print("\nRunning Energy Analysis...")
    energy_analysis()

    print("\nRunning Range Calculation...")
    df, summary = run(battery_capacity_kwh=battery, soc_percent=soc)

    print("\n----- RESULTS -----")
    print("Average Range:", summary["avg_range_km"], "km")
    print("Maximum Range:", summary["max_range_km"], "km")
    print("Minimum Range:", summary["min_range_km"], "km")


if __name__ == "__main__":
    start_interface()
