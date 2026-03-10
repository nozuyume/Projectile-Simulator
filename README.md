# Projectile Simulator

A Python-based projectile simulation pipeline for modeling 2D projectile motion with optional constant forces and linear air resistance. Built with a modular structure for input validation, simulation, and plotting.

## Project Structure

```text
projectile_simulator/
├── input_validator.py
├── main.py
├── requirements.txt
├── simulator.py
├── visualizer.py
└── __pycache__/
```

## Prerequisites

- Python 3.9+
- pip
- matplotlib 3.8.2

## Installation

```bash
git clone https://github.com/nozuyume/Projectile-Simulator
cd projectile_simulator
pip install -r requirements.txt
```

Or install dependency directly:

```bash
pip install matplotlib==3.8.2
```

## Usage

### Full Simulation

```bash
python main.py
```

You will be prompted to input:

- Initial velocity (m/s)
- Initial height (m)
- Launch angle (degrees)
- Mass (kg)
- Air resistance coefficient (kg/s)
- Time step (s)
- Maximum time steps
- Optional constant forces (magnitude and direction)

## Configuration

All physics and runtime parameters are entered through CLI prompts in main.py and validated by input_validator.py.

Simulation math is implemented in simulator.py, and plotting is handled by visualizer.py.

## Testing

No automated test suite is currently included.

You can do a quick manual run with:

```bash
python main.py
```
