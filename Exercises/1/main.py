import numpy as np
import pandas as pd

# reading data file
data_path = "data/data2.txt"
data_file = open(data_path, "r")
data_lines = data_file.readlines()

# preparing data
data = []
for line in data_lines:
    tmp_line = line.replace(" ", "")
    tmp_line = tmp_line.replace("\n", "")
    tmp_line = tmp_line.split(",")
    try:
        tmp_line = [float(x) for x in tmp_line]
    except:
        print("Invalid line in data file ...")
        exit()
    data.append(tmp_line)

print("\nData(Before standardize): ")
for i in range(len(data)):
    print(str(i+1) + ": " + str(data[i]))

# standardize data
max_len = max([len(x) for x in data])
for d in data:
    if len(d) < max_len:
        mean_d = np.mean(d)
        while len(d) < max_len:
            d.append(mean_d)

# covariance function
def cov(x, y):
    xbar, ybar = np.mean(x), np.mean(y)
    return np.sum((x - xbar)*(y - ybar))/(len(x) - 1)

# covariance matrix
def cov_mat(X):
    n = len(X)
    cov_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            cov_matrix[i, j] = cov(X[i], X[j])
    return cov_matrix

print("\nData(After standardize): ")
for i in range(len(data)):
    print(str(i) + ": " + str(data[i]))

covariance_matrix = cov_mat(data)
print("\nCovarinace matrix: ")
print(pd.DataFrame(covariance_matrix))