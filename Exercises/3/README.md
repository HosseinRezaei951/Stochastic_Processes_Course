# Birth-Death Process Simulation

## Overview

This assignment focuses on simulating a Birth-Death process using Python. The goal is to model how the population size evolves over time based on different birth and death rates. The script generates and visualizes multiple paths of population changes for varying rates, helping to understand the dynamics of such stochastic processes.

## Project Structure

The project includes the following directories and key files:

### Directories

- **results/**: Contains the output of the simulation, including visualizations.
  - **`result.jpeg`**: A plot showing the evolution of population sizes over time for various birth and death rates.

### Main Script

- **`main.py`**: The primary Python script that performs the following tasks:
  1. Simulates the Birth-Death process for different birth and death rates.
  2. Computes the evolution of the population size over time.
  3. Generates and saves visualizations showing the results for different parameter settings.

## Task Details

### Birth-Death Process Simulation

The script simulates the Birth-Death process using the following parameters:
- **`firstPopulation`**: Initial population size (set to 50).
- **`maxPopulation`**: Maximum allowable population size (set to 1000).
- **`nPath`**: Number of simulation paths to generate (set to 3).
- **`birthRates`**: A list of different birth rates to simulate.
- **`deathRates`**: A list of different death rates to simulate.

The function `birthDeath` calculates the population size over time for the given parameters using stochastic simulation techniques.

### Visualization

The script generates a matrix of plots, where each subplot represents a combination of birth and death rates. The plots show:
- The evolution of population size over time.
- Different paths of population changes for each combination of birth and death rates.

### Example Plot

- **Population Evolution**:

  ![Population Evolution](https://github.com/HosseinRezaei951/Stochastic_Processes_Course/blob/main/Exercises/3/results/result.jpeg)

  The plot visualizes how the population size evolves over time for various birth and death rates. The results illustrate the impact of varying these rates on population dynamics.

## How to Use

1. **Prepare the Script**:
   - Ensure that the required libraries (Numpy and Matplotlib) are installed in your Python environment.

2. **Run the Script**:
   - Execute `main.py` to perform the simulation and generate the results.
   - The script will compute the population dynamics and save the visualization in the `results/` directory as `result.jpeg`.

3. **View Results**:
   - Check `results/result.jpeg` for the visualization of the simulated Birth-Death processes.

## Conclusion

This assignment provides practical experience with simulating stochastic processes, specifically the Birth-Death process, using Python. By analyzing the effects of different birth and death rates on population size, you gain insights into the behavior and dynamics of such processes. The visualizations offer a comprehensive view of how varying parameters influence the system over time.