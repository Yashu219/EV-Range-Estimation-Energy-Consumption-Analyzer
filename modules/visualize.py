from modules.visualization import (
    plot_speed_vs_consumption,
    plot_distance_vs_consumption
)

speed = [20, 40, 60, 80, 100]
consumption_speed = [90, 110, 130, 160, 200]

distance = [5, 10, 20, 40, 60]
consumption_distance = [95, 105, 120, 140, 160]

plot_speed_vs_consumption(speed, consumption_speed)
plot_distance_vs_consumption(distance, consumption_distance)
