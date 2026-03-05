Projectile Simulator
====================

Overview
--------
This program simulates 2D projectile motion over time and plots the trajectory.
You provide launch settings and optional constant external forces. The simulator
computes position and velocity at each time step, prints the trajectory data,
and displays a graph using Matplotlib.

Files
-----
- main.py
  Entry point. Collects input, runs the simulation, prints trajectory output,
  and launches visualization.

- input_validator.py
  Validates numeric input ranges and handles optional force entry.

- simulator.py
  Performs time-step physics updates for velocity and position and returns the
  trajectory list.

- visualizer.py
  Plots projectile path (distance vs. height) using Matplotlib.

How It Works
------------
1. Enter initial velocity, launch angle, mass, time step, and max time steps.
2. Optionally add one or more constant forces (magnitude + direction).
3. The simulator updates motion each step using:
   - Net force -> acceleration
   - Acceleration -> velocity
   - Velocity -> position
4. Simulation stops when max steps are reached or the projectile drops below
   ground level (y < 0).
5. Trajectory data is printed and then visualized.

Inputs
------
Prompted in this order:
- Initial velocity (m/s), must be >= 0
- Launch angle (degrees), must be between -180 and 180
- Mass (kg), must be >= 0
- Time step (s), must be >= 0
- Maximum time steps, must be >= 1
- Optional forces:
  - Add force? (y/n)
  - Magnitude (N), must be >= 0
  - Direction (degrees), must be between -180 and 180

Output
------
- Printed trajectory list of tuples:
  (time, x_position, y_position, x_velocity, y_velocity)
- Matplotlib plot window showing the projectile trajectory

Requirements
------------
- Python 3.x
- matplotlib

Install dependency:
  pip install matplotlib

Run
---
From the project folder:
  python main.py

Notes
-----
- Gravity is set to 9.81 m/s^2 in the simulation function.
- Force directions are entered in degrees and converted internally to radians.
