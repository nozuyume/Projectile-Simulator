import matplotlib.pyplot as plt

def visualize(positions):
    """
    Visualizes the trajectory of the projectile
    using matplotlib.
    """
    x_vals = [pos[1] for pos in positions]
    y_vals = [pos[2] for pos in positions]
    
    plt.figure(figsize=(10, 5))
    plt.plot(x_vals, y_vals, marker='o')
    plt.title('Projectile Trajectory')
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.grid()
    plt.show(block=True)