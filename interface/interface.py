from modules.range_calculation import run
from modules.energy_analysis import energy_analysis
from modules.visualization import (
    plot_speed_vs_consumption,
    plot_distance_vs_consumption
)


def start_interface():
    print("EV Range Estimation & Energy Analyzer")
    print("-------------------------------------")

    battery = float(input("Enter Battery Capacity (kWh): "))
    soc = float(input("Enter State of Charge (%): "))

    print("\nRunning Energy Analysis...")
    energy_analysis()

    print("\nRunning Range Calculation...")
    df, summary = run(battery_capacity_kwh=battery, soc_percent=soc)

    print("\n----- RANGE RESULTS -----")
    print("Average Range:", summary["avg_range_km"], "km")
    print("Maximum Range:", summary["max_range_km"], "km")
    print("Minimum Range:", summary["min_range_km"], "km")

    print("\nGenerating Graphs...")

    # sample data for graphs
    speed = [20, 40, 60, 80, 100]
    consumption_speed = [90, 110, 130, 160, 200]

    distance = [5, 10, 20, 40, 60]
    consumption_distance = [95, 105, 120, 140, 160]

    plot_speed_vs_consumption(speed, consumption_speed)
    plot_distance_vs_consumption(distance, consumption_distance)


if __name__ == "__main__":
    start_interface()
