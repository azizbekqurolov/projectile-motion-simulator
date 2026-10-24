
import math
import numpy as np
import matplotlib.pyplot as plt


# -------------------------
# Initial conditions
# -------------------------
while True:
    try:
        initial_velocity = float(input("Enter the initial velocity (m/s): "))
        launch_angle = float(input("Enter the launch angle (degrees): "))
        if initial_velocity <= 0 or launch_angle <= 0 or launch_angle >= 90:
            print("Please enter a positive initial velocity and an angle between 0 and 90 degrees.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter numeric values.")
gravity = 9.81         # m/s^2


# -------------------------
# Velocity components
# -------------------------

def horizontal_velocity():
    # Convert the angle from degrees to radians
    radians = math.radians(launch_angle)

    # Calculate horizontal velocity using cosine
    h_vel = initial_velocity * math.cos(radians)

    return h_vel


def vertical_velocity():
    # Convert the angle from degrees to radians
    radians = math.radians(launch_angle)

    # Calculate vertical velocity using sine
    v_vel = initial_velocity * math.sin(radians)

    return v_vel


# -------------------------
# Flight calculations
# -------------------------

def flight_time():
    # Calculate total time in the air
    time = 2 * vertical_velocity() / gravity

    return time


def maximum_height():
    # Calculate maximum height
    height = vertical_velocity() ** 2 / (2 * gravity)

    return height


def horizontal_range():
    # Calculate horizontal distance travelled
    distance = horizontal_velocity() * flight_time()

    return distance


# -------------------------
# Display calculated results
# -------------------------

print("=" * 40)
print("PROJECTILE MOTION SIMULATOR")
print("=" * 40)

print(f"Horizontal velocity: {horizontal_velocity():.2f} m/s")
print(f"Vertical velocity:   {vertical_velocity():.2f} m/s")
print(f"Flight time:         {flight_time():.2f} s")
print(f"Maximum height:      {maximum_height():.2f} m")
print(f"Horizontal range:    {horizontal_range():.2f} m")


# -------------------------
# Generate trajectory data
# -------------------------

# Generate 100 evenly spaced time values
time_values = np.linspace(0, flight_time(), 100)

# Calculate horizontal and vertical positions
x_positions = horizontal_velocity() * time_values

y_positions = (
    vertical_velocity() * time_values
    - 0.5 * gravity * time_values**2
)

# -------------------------
# Plot the trajectory
# -------------------------

plt.scatter(
    horizontal_range() / 2,
    maximum_height(),
    color="blue",
    label="Maximum height",
    zorder=3
)

plt.plot(x_positions, y_positions, linewidth=2, color='red')
plt.xlabel("Horizontal Distance (m)", color='blue')
plt.ylabel("Vertical Distance (m)", color='blue')
plt.title("Projectile Trajectory", color='green')
plt.grid(True)
plt.legend()
plt.show()