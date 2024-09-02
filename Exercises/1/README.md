# Covariance Matrix Computation for Sensor Data

## Overview

This assignment focuses on computing the covariance matrix for data collected from multiple sensors. Each sensor collects one-dimensional data over time, and the goal is to standardize this data to a common length and then calculate the covariance matrix to understand the relationships between different sensors' data. This task is implemented in Python, and the script includes detailed explanations and results for different datasets.

## Project Structure

The project includes the following directories and key files:

### Directories

- **data/**: Contains the raw datasets used for computation.
  - `data1.txt`: A text file containing sensor data for the first test case.
  - `data2.txt`: A text file containing sensor data for the second test case.

- **results/**: Contains the results of the covariance matrix computation, including the covariance matrices for different datasets. (Note: This directory may be created based on future needs to store results.)

### Main Script

- **main.py**: The primary Python script that performs the following tasks:
  1. Reads and prepares the sensor data from text files.
  2. Standardizes the data to ensure all sensor data arrays have the same length.
  3. Computes the covariance matrix for the standardized data.
  4. Prints the covariance matrix to the console.

## Task Details

### Data Preparation

The script reads sensor data from text files, where each line represents data collected from a different sensor. It then standardizes the data by extending shorter sensor data arrays to match the length of the longest array, using the mean of the existing data to fill in the gaps.

### Covariance Matrix Calculation

The script defines a `cov()` function to calculate the covariance between two data vectors and a `cov_mat()` function to generate the covariance matrix for the entire dataset. The covariance matrix reveals how changes in one sensor's data are related to changes in another's.

### Results

The results of the covariance matrix computation are displayed for different datasets. The matrices illustrate the degree of correlation between the sensor data arrays.

Below are examples of the results:

- **Results for `data1.txt`**:
  - The covariance matrix for this dataset will be displayed, showing the covariance values between different sensors' data.

- **Results for `data2.txt`**:
  - The covariance matrix for this dataset will also be displayed, highlighting the relationships between sensor data collected in different formats.

## How to Use

1. **Run the Script**:
   - Execute `main.py` to perform the data preparation, standardization, and covariance matrix computation.
   - The script will print the covariance matrix to the console.

2. **View Results**:
   - The output will include the covariance matrices for the datasets provided in `data/`. Ensure the sensor data files (`data1.txt` and `data2.txt`) are correctly formatted and placed in the `data/` directory.

## Conclusion

This assignment provides practical experience in handling and analyzing sensor data using Python. By computing the covariance matrix, you gain insights into how different sensors' data are interrelated, which is crucial for understanding the underlying processes and improving data analysis methodologies. The provided script ensures that you can easily adapt the analysis to different datasets by simply modifying the input files.