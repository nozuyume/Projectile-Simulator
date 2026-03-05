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
        net_fx += mag * math.cos(dir_deg)
        net_fy += mag * math.sin(dir_deg)
    return net_fx, net_fy

def simulation(v0, angle, mass, dt, forces, maxtime, g=9.81):
    """
    Calculates the velocity, acceleration,
    and position of the projectile at each time step.
    """
    x = 0.0
    y = 0.0
    vx = v0 * math.cos(math.radians(angle))
    vy = v0 * math.sin(math.radians(angle))
    t = 0.0

    trajectory = []

    for _ in range(maxtime):
        trajectory.append((t, x, y, vx, vy))

        fx, fy = sum_forces(forces)
        ax = fx / mass
        ay = (fy / mass) - g

        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt
        t += dt

        if y < 0:
            break

    trajectory_set = set(trajectory)
    return trajectory, trajectory_set