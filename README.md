# Stochastic Processes Course

Welcome to the Stochastic Processes Course repository. This repository contains a series of exercises aimed at understanding and applying stochastic processes through practical Python implementations. Each exercise focuses on different aspects of stochastic processes, including Markov chains, Birth-Death processes, and covariance matrix computations. The provided scripts and datasets will help you gain hands-on experience with these concepts.

## Directory Structure

### Exercises

The `Exercises` directory is organized into subdirectories, each corresponding to a different assignment:

#### Exercise 1: Covariance Matrix Computation for Sensor Data

This exercise involves computing the covariance matrix for data collected from multiple sensors:

- **Data Directory**:
  - Contains sensor data files used for the covariance matrix computation.
  
- **Scripts**:
  - **`main.py`**: Script to read sensor data, standardize it, and calculate the covariance matrix.

- **README.md**: Provides an overview of the exercise, including instructions and results.

#### Exercise 2: Markov Chain Analysis

This exercise focuses on analyzing a Markov chain by computing and visualizing state probabilities over time:

- **Data Directory**:
  - Contains an input file with initial state probabilities, transition matrix, and number of days for simulation.

- **Scripts**:
  - **`main.py`**: Script to simulate the Markov chain and visualize the state probabilities over time.

- **Figures**:
  - **`Figure_1.png`**: Plot showing the evolution of state probabilities for different initial conditions.

- **README.md**: Provides an overview of the exercise, including instructions and the results.

#### Exercise 3: Birth-Death Process Simulation

This exercise simulates a Birth-Death process to model population size changes over time with varying birth and death rates:

- **Results Directory**:
  - Contains visualizations of the population size evolution over time.

- **Scripts**:
  - **`main.py`**: Script to simulate the Birth-Death process and generate plots showing population dynamics.

- **README.md**: Provides an overview of the exercise, including instructions and the results.

## How to Use

### Running the Scripts

1. **Exercise 1 (Covariance Matrix Computation)**:
   - Navigate to the `1` subdirectory and run `main.py` to perform the covariance matrix computation on the provided sensor data.

2. **Exercise 2 (Markov Chain Analysis)**:
   - Navigate to the `2` subdirectory and execute `main.py` to simulate the Markov chain and generate visualizations based on the input data in `data/input.txt`.

3. **Exercise 3 (Birth-Death Process Simulation)**:
   - Navigate to the `3` subdirectory and run `main.py` to simulate the Birth-Death process and view the results in `results/result.jpeg`.

## Conclusion

This repository provides practical exercises to deepen your understanding of stochastic processes through Python simulations. By working through these exercises, you will gain insights into Markov chains, Birth-Death processes, and covariance matrix computations. The provided scripts and visualizations offer a comprehensive learning experience, helping you apply stochastic process concepts to real-world scenarios. Feel free to explore and modify the code to further enhance your understanding and adapt the techniques to different datasets.