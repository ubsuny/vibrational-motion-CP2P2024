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

print(nol_low)
print(nol_up)

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
