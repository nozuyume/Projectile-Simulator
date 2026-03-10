import input_validator
import simulator
import visualizer
import math

if __name__ == "__main__":
    """
    Collects user input for constant values,
    then prints the trajectory and visualizes it.
    """
    print("Input your initial values.")
    v0 = input_validator.get_float_input("Initial velocity (m/s): ", min_val=0)
    angle = input_validator.get_float_input("Launch angle (degrees): ", min_val=-180, max_val=180)
    mass = input_validator.get_float_input("Mass (kg): ", min_val=0)
    dt = input_validator.get_float_input("Time step (s): ", min_val=0)
    maxtime = int(input_validator.get_float_input("Maximum time steps: ", min_val=1))
    forces = input_validator.get_forces()
    trajectory, trajectory_set = simulator.simulation(v0, angle, mass, dt, forces, maxtime)
    print(f"{trajectory}")
    visualizer.visualize(trajectory)