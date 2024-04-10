# Using Tensorflow in existing code
```python
import tensorflow as tf
import numpy as np

# Read lines from file
with open("frame_s.asc", 'r') as fi1:
    lines1 = fi1.readlines()

band_low = 0.04 # set lower boundary
band_up = 0.05 # set upper boundary
nol_low = -1  # find the line in input which represents the lower boundary
nol_up = -1  # upper boundary
for i, line in enumerate(lines1):
    freq_cur = float(line.split()[0])
    if freq_cur > band_low and nol_low == -1:
        nol_low = i
    if freq_cur > band_up and nol_up == -1:
        nol_up = i - 1
        break


# Load data using TensorFlow
a = np.load("frame_U.npz")
Mat = tf.constant(a['arr_0'], dtype=tf.float32)

# Prepare displacement list
disp = [[] for _ in range(nol_up - nol_low + 1)]

# Read lines from PDB file
with open("deleted.pdb", 'r') as pdb:
    pdblines = pdb.readlines()

for line in pdblines:
    words = line.split()
    if len(words) < 1:
        pass
    elif words[0] == "ATOM":
        atomname = line[13:16].strip()
        if atomname == "CA":
            resid = line[22:26].strip()
            atomnumber = int(line[5:11].strip())
            for j in range(nol_up - nol_low + 1):
                disp[j].append([
                    Mat[atomnumber * 3 - 3, j + nol_low],
                    Mat[atomnumber * 3 - 2, j + nol_low],
                    Mat[atomnumber * 3 - 1, j + nol_low]
                ])

# Calculate correlations using TensorFlow
disp = tf.constant(disp, dtype=tf.float32)
corre = tf.einsum('ijk,ilk->ijl', disp, disp)

# Save correlation matrix
np.save("correlation_4to5.npy", corre.numpy())
```










### Step 1: Reading Data
- The code begins by reading data from two files: "frame_s.asc" and "deleted.pdb".
- The contents of "frame_s.asc" are read line by line to determine the lower and upper boundaries based on frequency values.
- The frequency values determine the time intervals for which the displacement data will be analyzed.

### Step 2: Loading Data with TensorFlow
- Using TensorFlow, the displacement data is loaded from a NumPy file ("frame_U.npz").
- The displacement data represents the movement of particles or atoms over time.

### Step 3: Preparing Data for Analysis
- The displacement data is organized into a list of lists, where each inner list contains displacement vectors corresponding to a specific time interval.

### Step 4: Processing PDB File
- The PDB file ("deleted.pdb") contains information about atoms or particles.
- Relevant information is extracted from the PDB file, specifically focusing on atoms named "CA" (alpha carbon atoms).

### Step 5: Calculating Correlations with TensorFlow
- TensorFlow's `tf.constant` function is used to convert the displacement data into TensorFlow tensors, which can be efficiently processed within TensorFlow.
- The displacement tensors are then used to calculate correlations using `tf.einsum`, which computes the dot product of displacement vectors for each pair of time steps.
- This results in a correlation matrix representing the degree of correlation between displacement vectors at different time intervals.

### Step 6: Saving Results
- Finally, the correlation matrix is saved to a NumPy file ("correlation_4to5.npy") using NumPy's `np.save` function.
- The saved correlation matrix can be further analyzed or visualized for insights into the dynamics of the system.


### Result 
![Correlation plot for frequency range 4 to 5](https://github.com/ubsuny/vibrational-motion-CP2P2024/blob/main/plot4%20(1).png)



### Conclusion
- The code demonstrates how TensorFlow can be integrated with other Python libraries, such as NumPy, for data processing and analysis tasks.
- By leveraging TensorFlow's efficient tensor operations, complex computations, such as calculating correlations, can be performed effectively on large datasets.
- The run time for the previous code was 12 minutes and for this code it is also the same. So there is no difference in execution time while using the tensorflow.
