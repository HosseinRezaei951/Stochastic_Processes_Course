# Markov Chain Analysis

## Overview

This assignment involves analyzing a Markov chain over a specified number of days using Python. The objective is to compute and visualize the state probabilities after a series of transitions, given an initial state and a transition matrix. Additionally, the assignment explores the long-term behavior of the Markov chain and its convergence based on the provided transition matrix.

## Project Structure

The project includes the following directories and key files:

### Directories

- **data/**: Contains the input data file used for computations.
  - **`input.txt`**: Text file with the initial state probabilities, transition matrix, and number of days to simulate.

- **results/**: (Note: This directory may be created based on future needs to store results such as generated figures or output files.)

### Main Script

- **`main.py`**: The primary Python script that performs the following tasks:
  1. Reads input data from `input.txt`.
  2. Initializes the transition matrix and initial state probabilities.
  3. Computes the state probabilities over the specified number of days.
  4. Visualizes the results with plots showing how the probabilities evolve over time.

### Output

- **`Figure_1.png`**: A plot showing the evolution of state probabilities over time.



## Task Details

### Input Data

The input data consists of:
1. **Number of Days** (`nDay`): Specifies the number of days for the Markov chain simulation.
2. **Initial State Probabilities** (`P_start`): The probabilities of being in each state at day 0.
3. **Transition Matrix** (`P`): Defines the probabilities of transitioning from one state to another.

### Computation and Visualization

The script performs the following steps:
1. **Read Input Data**: Reads the number of days, initial state probabilities, and transition matrix from `input.txt`.
2. **Compute State Probabilities**: Uses matrix multiplication to calculate the state probabilities over each day.
3. **Plot Results**: Generates a plot showing the evolution of state probabilities over time for two different initial states:
   - **Initial State [1, 0]**: Starting from a fully "happy" state.
   - **Initial State [0, 1]**: Starting from a fully "sad" state.

### Example Plot

- **Probability Evolution**:

  ![Probability Evolution](https://github.com/HosseinRezaei951/Stochastic_Processes_Course/blob/main/Exercises/2/Figure_1.png)

  The plot shows how the probability of being in each state evolves over time for different initial conditions. 

## How to Use

1. **Prepare the Input File**:
   - Ensure `input.txt` is correctly formatted and located in the `data/` directory.

2. **Run the Script**:
   - Execute `main.py` to perform the computations and generate visualizations.
   - The script will read data from `input.txt`, compute the state probabilities over the specified number of days, and display the results as plots.

3. **View Results**:
   - The generated plot will show the state probabilities' evolution over time based on the initial conditions and transition matrix.
   - Check `Figure_1.png` in the `results/` directory (or where the script saves it) for the visual output.

## Conclusion

This assignment provides hands-on experience with Markov chains and their analysis using Python. By simulating the Markov process over a set number of days and visualizing the results, you gain insights into how state probabilities change over time and the long-term behavior of the chain. The provided script and visualizations help in understanding the impact of initial states and transition probabilities on the system's evolution.