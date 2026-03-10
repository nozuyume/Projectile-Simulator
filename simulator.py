import math

def sum_forces(forces):
    """
    Sums up the forces of the magnitudes
    and angles of directions in the forces
    list.
    """
    net_fx = 0.0
    net_fy = 0.0
    for mag, dir_deg in forces:
        math.radians(dir_deg)
        net_fx += mag * math.cos(dir_deg)
        net_fy += mag * math.sin(dir_deg)
    return net_fx, net_fy

def simulation(v0, angle_deg, y0, mass, b, dt, max_time, forces):
    """
    Simulates projectile motion with air resistance and external forces.
    """
    
    g=9.81
    angle_rad = math.radians(angle_deg)
    
    # initial conditions
    x = 0.0
    y = y0
    vx = v0 * math.cos(angle_rad)
    vy = v0 * math.sin(angle_rad)
    t = 0.0

    """
    Trajectory lists
    Used in analyze_simulation for max height and range,
    and in visualizer for plotting the trajectory.
    """
    xs = [x]
    ys = [y]
    
    # constant forces
    net_fx, net_fy = sum_forces(forces)

    """
    While loop:
    continues while projectile doesn't hit the ground
    and while time doesn't exceed max_time.
    """
    while y >= 0 and t <= max_time:
        ax = net_fx / mass - b * vx
        ay = (net_fy - b * vy - mass * g) / mass

        """
        Euler integration
        Updates velocity, then the position and time.
        """
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt
        t += dt

        xs.append(x)
        ys.append(y)
    
    """
    if the projectile goes below ground level,
    it removes the last point from the trajectory lists
    and subtracts the last time step from t.
    """
    if y < 0 and len(xs) > 1:
        xs.pop()
        ys.pop()
        t -= dt

    return xs, ys, t

def analyze_simulation(xs, ys):
    """
    Gets the highest y value for max height
    and the highest x value for max range.
    """

    """
    If the lists are empty,
    this returns 0 for both xs and ys.
    """
    if not xs or not ys:
        return 0.0, 0.0

    """
    Scans the list for the max y value.
    If the next y value is higher than max_height,
    it assigns it to max_height.
    """
    max_height = ys[0]
    for i in range(1, len(ys)):
        if ys[i] > max_height:
            max_height = ys[i]


    """
    Scans the list for the max x value.
    If the next x value is higher than max_range,
    it assigns it to max_range.
    """
    max_range = xs[0]
    for i in range(1, len(xs)):
        if xs[i] > max_range:
            max_range = xs[i]

    return max_height, max_range
