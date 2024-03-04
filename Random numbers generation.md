# Random Numbers in My Project

My project is to determine the frequency dependence of the average root mean squared displacements of the waters in the calculations of the vibrations of the hydrated proteins. In my data set, I have the frequencies in the columns and eigenvectors associated with the frequencies in the rows. So I need to find the rmsd from the given data points. I am using machine learning for the findings. So I will be generating training and testing data sets randomly. I will train 80% of the data set and the rest 20% data will be tested using the train_test_split function from sklearn.model_selection.

First of all,  a linear regression model using LinearRegression() from sklearn.linear_model will be initialized and then, we train the model using the training data (X_train and y_train) with the fit() method.

### Randomness in Data Splitting:

When splitting the data into training and testing sets (or for cross-validation), the train_test_split function from sklearn.model_selection randomly shuffles the data before splitting.
This random shuffling ensures that the data points are randomly distributed between the training and testing sets, reducing the risk of introducing biases in the model evaluation process.

```python
import numpy as np
from sklearn.model_selection import train_test_split

def calculate_rmsd(config1, config2):
    """
    Calculate the Root Mean Square Deviation (RMSD) between two configurations.
    
    Parameters:
    - config1: numpy array representing the coordinates of the first configuration
    - config2: numpy array representing the coordinates of the second configuration
    
    Returns:
    - rmsd: Root Mean Square Deviation between the two configurations
    """
    diff = config1 - config2
    squared_diff = np.square(diff)
    mean_squared_diff = np.mean(squared_diff)
    rmsd = np.sqrt(mean_squared_diff)
    return rmsd

# Given data
data = np.array([[1.79e-03, 2.63e-03, -3.57e-03, -1.43e-03, -1.96e-03, 2.10e-03, 6.70e-04, -2.04e-03, -1.37e-03, -1.77e-03],
                 [2.86e-03, -2.30e-04, -2.38e-03, 1.35e-03, 3.34e-03, 1.60e-04, 2.20e-04, -2.67e-03, -1.33e-03, 4.50e-04],
                 [-2.61e-03, 1.47e-03, -4.90e-04, 3.84e-03, -1.91e-03, 7.70e-04, -9.30e-04, 9.30e-04, 2.54e-03, 1.30e-04],
                 [1.74e-03, 2.54e-03, -3.57e-03, -1.43e-03, -1.96e-03, 1.88e-03, 9.20e-04, -1.85e-03, -1.17e-03, -1.70e-03],
                 [2.58e-03, -2.10e-04, -2.38e-03, 1.35e-03, 3.34e-03, 1.40e-04, 2.20e-04, -2.50e-03, -9.80e-04, 5.20e-04],
                 [-2.55e-03, 1.43e-03, -4.90e-04, 3.84e-03, -1.91e-03, 6.80e-04, -8.30e-04, 9.60e-04, 2.53e-03, 1.40e-04],
                 [1.74e-03, 2.56e-03, -3.57e-03, -1.43e-03, -1.96e-03, 2.11e-03, 6.40e-04, -1.99e-03, -1.32e-03, -1.77e-03],
                 [3.02e-03, -2.00e-05, -2.38e-03, 1.35e-03, 3.34e-03, 1.40e-04, 3.10e-04, -2.82e-03, -1.50e-03, 4.40e-04],
                 [-2.52e-03, 1.46e-03, -4.90e-04, 3.84e-03, -1.91e-03, 1.02e-03, -1.15e-03, 8.20e-04, 2.23e-03, -1.00e-05],
                 [1.96e-03, 2.85e-03, -3.57e-03, -1.43e-03, -1.96e-03, 2.11e-03, 7.90e-04, -2.15e-03, -1.67e-03, -1.80e-03]])

# Generating random indices for splitting the data
num_samples = data.shape[0]
indices = np.random.permutation(num_samples)

# Calculate RMSD for each configuration
reference_config = data[0]  # Use the first configuration as the reference
rmsd_values = [calculate_rmsd(reference_config, config) for config in data]

# Convert rmsd_values to numpy array
rmsd_values = np.array(rmsd_values)

# Splitting the data into features (frequencies) and labels (RMSD values)
X = data  # Features (frequencies)
y = rmsd_values  # Labels (RMSD values)

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

```

Above shown is the code snippet of the splitting of the data sets where random numbers are used. I have taken some datas from my data sets and used that to check wether the code runs.
