# Projectile Motion Simulator

A physics-based projectile motion simulator built with Python.

This is my second scientific computing project. I built it to strengthen my understanding of classical mechanics, mathematical modeling, Python functions, NumPy arrays, and data visualization using Matplotlib.

## Features

The simulator calculates and visualizes projectile motion based on the initial velocity and launch angle.

It supports:

1. Initial velocity input (m/s)
2. Launch angle input (degrees)
3. Horizontal velocity
4. Vertical velocity
5. Total flight time
6. Maximum height
7. Horizontal range
8. Trajectory data generation using NumPy
9. Projectile trajectory visualization using Matplotlib
10. Maximum-height marker on the trajectory graph
11. Input validation and error handling

## Physics and Equations

The simulator uses the equations of ideal projectile motion.

### Velocity Components

Horizontal velocity:

\[
v_x = v_0\cos(\theta)
\]

Vertical velocity:

\[
v_y = v_0\sin(\theta)
\]

### Flight Time

\[
T = \frac{2v_0\sin(\theta)}{g}
\]

### Maximum Height

\[
H = \frac{v_0^2\sin^2(\theta)}{2g}
\]

### Horizontal Range

\[
R = \frac{v_0^2\sin(2\theta)}{g}
\]

### Trajectory Equations

Horizontal position:

\[
x(t) = v_0\cos(\theta)t
\]

Vertical position:

\[
y(t) = v_0\sin(\theta)t-\frac{1}{2}gt^2
\]

The simulation assumes constant gravitational acceleration of \(9.81\text{ m/s}^2\), ignores air resistance, and assumes the projectile lands at its launch height.

## Error Handling

The simulator handles several invalid inputs, including:

- Non-numeric input
- Negative initial velocity
- Launch angles outside the accepted range

## Technologies

- Python 3
- `math` module
- NumPy
- Matplotlib
- VS Code

## Python Concepts Practiced

Through this project, I practiced:

- Variables and data types
- User input and type conversion
- Functions and return values
- Trigonometric calculations
- Degrees-to-radians conversion
- Mathematical modeling
- NumPy arrays and `linspace()`
- Vectorized calculations
- Data visualization with Matplotlib
- Input validation
- Exception handling with `try` and `except`
- Scientific plotting and labeling

## How to Run

1. Make sure Python 3 is installed.
2. Clone this repository.
3. Open the project folder.
4. Install the required libraries:

```bash
python -m pip install numpy matplotlib
```

5. Run the simulator:

```bash
python projectile_motion.py
```

6. Enter the initial velocity and launch angle when prompted.

## Project Structure

```text
Projectile Motion Simulator/
├── projectile_motion.py
└── README.md
```

## Example

The simulator can be used like this:

```text
Enter the initial velocity (m/s): 20
Enter the launch angle (degrees): 45
```

Expected results (approximately):

```text
Horizontal velocity: 14.14 m/s
Vertical velocity:   14.14 m/s
Flight time:         2.88 s
Maximum height:      10.19 m
Horizontal range:    40.77 m
```

The program also generates a graph showing the projectile's trajectory and its maximum height.

## Future Improvements

Possible future improvements include:

- Comparing trajectories at different launch angles
- Animating projectile motion
- Adding air resistance
- Comparing numerical simulations with analytical results

## Author

Azizbek Qurolov

This project was created as part of my journey toward learning Python and developing programming skills for future work in aerospace engineering and scientific computing.