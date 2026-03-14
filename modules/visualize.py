import matplotlib.pyplot as plt


def plot_speed_vs_consumption(speed, consumption):
    plt.figure()
    plt.plot(speed, consumption, marker='o')
    plt.title("Speed vs Energy Consumption")
    plt.xlabel("Speed (km/h)")
    plt.ylabel("Consumption (Wh/km)")
    plt.grid(True)
    plt.show()


def plot_distance_vs_consumption(distance, consumption):
    plt.figure()
    plt.plot(distance, consumption, marker='o')
    plt.title("Distance vs Energy Consumption")
    plt.xlabel("Distance (km)")
    plt.ylabel("Consumption (Wh/km)")
    plt.grid(True)
    plt.show()
