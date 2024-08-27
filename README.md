# Eukaryotic Cell Simulation

This project simulates the basic functions of a eukaryotic cell using Python. The simulation includes organelle activities and cell processes, such as protein synthesis, energy production, lysosome function, and cell division (mitosis).
I'll be adding more things, like simulating more life processes eventually.
## Features

- **Organelle Simulation**: Simulates the functions of key organelles including:
  - Nucleus: Controls cell activities.
  - Mitochondria: Produces energy.
  - Smooth ER (SER): Synthesizes lipids.
  - Golgi Apparatus: Processes proteins.
  - Lysosome: Breaks down waste.
- **Cell Processes**:
  - **Protein Synthesis**: Activated every 5 ticks.
  - **Energy Production**: Activated every 10 ticks.
  - **Lysosome Function**: Activated every 15 ticks.
  - **Mitosis**: Activated every 20 ticks, creating a new cell.

## Requirements

- Python 3.11

## Installation

Clone the repository and run the simulation script:

```bash
git clone https://github.com/zeusssz/life-py.git
cd life-py
python main.py
```

## Usage

1. **Run the Simulation**: Execute the script using Python.
2. **Observe the Output**: The simulation will print the status of organelles and cell processes to the terminal.

## Example Output

```
Nucleus is performing: Controls cell activities
Smooth ER is performing: Synthesizes lipids
Golgi Apparatus is performing: Processes proteins
Mitochondria is performing: Produces energy
Lysosome is performing: Breaks down waste
Mitosis activated: New cell created.
Creating organelles for new cell. Total cells: 2
```

## Notes
- The `tick()` method updates the state of the cell and its organelles every second.
