"""
range_calculation.py
Member 2 - Range Calculation Module
EV Range Estimation & Energy Consumption Analyzer
"""

import pandas as pd


def load_data(filepath="data/ev_data.csv"):
    df = pd.read_csv(filepath)
    df.columns = df.columns.str.strip()
    print(f"✅ Data loaded: {len(df)} records found.")
    return df


def calculate_range(df, battery_capacity_kwh=40.0, soc_percent=100.0):
    usable_energy_kwh = battery_capacity_kwh * (soc_percent / 100)

    df["Range_km"] = df["Consumption"].apply(
        lambda c: round(usable_energy_kwh / c, 2) if c > 0 else 0
    )

    print(f"\n⚡ Battery Capacity : {battery_capacity_kwh} kWh")
    print(f"🔋 SOC              : {soc_percent}%")
    print(f"📦 Usable Energy    : {usable_energy_kwh} kWh\n")

    return df


def summarize(df):
    avg_range = round(df["Range_km"].mean(), 2)
    max_range = round(df["Range_km"].max(), 2)
    min_range = round(df["Range_km"].min(), 2)
    avg_consumption = round(df["Consumption"].mean(), 4)
    avg_speed = round(df["Speed"].mean(), 2)

    print("=" * 40)
    print("       RANGE CALCULATION SUMMARY")
    print("=" * 40)
    print(f"  Average Range        : {avg_range} km")
    print(f"  Maximum Range        : {max_range} km")
    print(f"  Minimum Range        : {min_range} km")
    print(f"  Avg Consumption      : {avg_consumption} kWh/km")
    print(f"  Average Speed        : {avg_speed} km/h")
    print("=" * 40)

    summary = {
        "avg_range_km": avg_range,
        "max_range_km": max_range,
        "min_range_km": min_range,
        "avg_consumption_kwh_per_km": avg_consumption,
        "avg_speed_kmph": avg_speed,
    }

    return summary


def save_results(df, output_path="data/range_results.csv"):
    df.to_csv(output_path, index=False)
    print(f"\n💾 Results saved to: {output_path}")


def run(battery_capacity_kwh=40.0, soc_percent=100.0, filepath="data/ev_data.csv"):
    df = load_data(filepath)
    df = calculate_range(df, battery_capacity_kwh, soc_percent)
    summary = summarize(df)
    save_results(df)
    return df, summary


if __name__ == "__main__":
    df, summary = run(battery_capacity_kwh=40.0, soc_percent=80.0)
    print("\nSample Output (first 5 rows):")
    print(df[["Speed", "Distance", "Consumption", "Range_km"]].head())