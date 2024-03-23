# Random Numbers in My Project

My project is to determine the frequency dependence of the average root mean squared displacements of the waters in the calculations of the vibrations of the hydrated proteins. In my data set, I have the frequencies in the columns and eigenvectors associated with the frequencies in the rows. So I need to find the correlation between the displacement vectors and the frequencies.
### Randomness in Data Splitting:

When splitting the data into training and testing sets, the train_test_split function from sklearn.model_selection randomly shuffles the data before splitting.
This random shuffling ensures that the data points are randomly distributed between the training and testing sets, reducing the risk of introducing biases in the model evaluation process.
```python
import numpy as np
import matplotlib.pyplot as plt

# Provided eigen vectors
eigen_vectors = np.array([
    [ 1.79e-03,  2.63e-03, -3.57e-03, -1.43e-03, -1.96e-03,  2.10e-03,  6.70e-04, -2.04e-03, -1.37e-03, -1.77e-03],
    [ 2.86e-03, -2.30e-04, -2.38e-03,  1.35e-03,  3.34e-03,  1.60e-04,  2.20e-04, -2.67e-03, -1.33e-03,  4.50e-04],
    [-2.61e-03,  1.47e-03, -4.90e-04,  3.84e-03, -1.91e-03,  7.70e-04, -9.30e-04,  9.30e-04,  2.54e-03,  1.30e-04],
    [ 1.74e-03,  2.54e-03, -3.57e-03, -1.43e-03, -1.96e-03,  1.88e-03,  9.20e-04, -1.85e-03, -1.17e-03, -1.70e-03],
    [ 2.58e-03, -2.10e-04, -2.38e-03,  1.35e-03,  3.34e-03,  1.40e-04,  2.20e-04, -2.50e-03, -9.80e-04,  5.20e-04],
    [-2.55e-03,  1.43e-03, -4.90e-04,  3.84e-03, -1.91e-03,  6.80e-04, -8.30e-04,  9.60e-04,  2.53e-03,  1.40e-04],
    [ 1.74e-03,  2.56e-03, -3.57e-03, -1.43e-03, -1.96e-03,  2.11e-03,  6.40e-04, -1.99e-03, -1.32e-03, -1.77e-03],
    [ 3.02e-03, -2.00e-05, -2.38e-03,  1.35e-03,  3.34e-03,  1.40e-04,  3.10e-04, -2.82e-03, -1.50e-03,  4.40e-04],
    [-2.52e-03,  1.46e-03, -4.90e-04,  3.84e-03, -1.91e-03,  1.02e-03, -1.15e-03,  8.20e-04,  2.23e-03, -1.00e-05],
    [ 1.96e-03,  2.85e-03, -3.57e-03, -1.43e-03, -1.96e-03,  2.11e-03,  7.90e-04, -2.15e-03, -1.67e-03, -1.80e-03]
])

# Set random seed for reproducibility
np.random.seed(42)

# Create an array of indices
indices = np.arange(len(eigen_vectors))

# Shuffle the indices
np.random.shuffle(indices)

# Plot the shuffled indices
plt.figure(figsize=(8, 6))
plt.plot(indices, marker='o', linestyle='', markersize=5)
plt.title('Shuffled Indices')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)
plt.show()

```

![Nature of Randomness](https://github.com/ubsuny/vibrational-motion-CP2P2024/blob/main/random%20scatter.png) 

The plot shows the random shuffling of the indices. The x-axis represents the indices of the eigen vectors, and the y-axis represents the shuffled values of these indices.



### Randomness while taking snapshot of the video.
As I am studying vibrations of the protein, we determined the conformation of the protein by minimizing the potential energy. At room temperature, although being in its stable position, the protein starts waggling and shows many different configurations. We aim to generate the matrix for each of the configurations within a specific frequency range. So the configurational structure of the protein was chosen randomly during the waggling motion of the protein. The structure was randomly snapped from the video and the matrix for each of those structure needs to be calculated from which we can illustrate the correlation of frequency and other proteins character.

```python
import numpy as np

# Total number of snapshots or protein structures in the video
total_snapshots = 10000

# Number of snapshots to select randomly
num_selected_snapshots = 900

# Generate random indices representing the selected snapshots
random_indices = np.random.randint(0, total_snapshots, size=num_selected_snapshots)

# Print the randomly selected indices for illustration
print("Randomly selected indices:", random_indices)

x_coordinates = np.arange(num_selected_snapshots)

# Plot the randomly selected indices
plt.figure(figsize=(8, 6))
plt.scatter(x_coordinates, random_indices, marker='o', s=10)
plt.title('Randomly Selected Indices')
plt.xlabel('Snapshot')
plt.ylabel('Index')
plt.grid(True)
plt.show()

```
![Nature of Randomness](https://github.com/ubsuny/vibrational-motion-CP2P2024/blob/main/random%20snapshot.png)

There is no discernible pattern in the distribution of points. The points are scattered randomly across the plot without any apparent trend. This ensures that the analysis based on the selected snapshots is not biased towards specific configurations of the protein.



    
   



