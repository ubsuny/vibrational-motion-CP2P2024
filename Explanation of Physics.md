
# Explanation of Physics

The most probable structure of protein is frequently the most energetically favorable, i.e. the lowest energy. A protein’s structure is able to fluctuate. It is not as rigidly defined as a crystal object, allowing for both large and small fluctuations relative to the protein size. When proteins are frozen, the thermal energy is much lower which will cause the the protein to move toward one of the energy minina. However,at non-zero temperatures, the protein can still move in the energy landscape.This results in an ensemble of possible folded states, the distribution of which varies for each type of protein.

### Normal Mode Analysis
Normal mode analysis (NMA) is a computational technique widely employed in structural biology, computational chemistry, and materials science to investigate the vibrational motions and dynamics of molecules and molecular complexes. This method is rooted in the harmonic approximation, which posits that the potential energy surface governing atomic motion around their equilibrium positions is parabolic. NMA involves calculating the normal modes of a system, which represent the collective vibrational motions. Each normal mode is characterized by its frequency and associated vibrational pattern, depicting how atoms move relative to each other. These modes are determined by diagonalizing the mass-weighted Hessian matrix of the system, with the eigenvalues representing the squared frequencies and the eigenvectors describing the atomic displacements. In applications, NMA proves invaluable: in structural biology, it elucidates protein dynamics, including conformational changes and flexibility; in computational chemistry, it predicts vibrational spectra and analyzes molecular dynamics. 


The NMA method is most appropriate for modeling frozen samples, in which the structure is fairly ridged. At higher temperature the protein structure may occupy multiple conformations or move between structures due to the thermal energy. Each of these different structures each potentially have a different set of vibrational modes, due to the varying structures. Since the measurements  were performed at room temperature, and the samples contain a large concentration of proteins, it is necessary to include multiple protein conformations in the calculations. Normal mode analysis  performed on each minimized structure to obtain the vibrational mode frequencies, displacement vectors, and dipole derivative vectors. The eigenvectors indicate the atomic displacement of each atom in the molecule throughout the mode’s motion. The dipole derivative is related to the net displacement of the charge during the motion.

## Necessity of this study:
NMA includes the motions of the solvent in the calculation. Therefore for all calculated modes, the solvent around the protein moves in concert with the protein motion. This may lead to a double counting of some protein motions in which the solvent moves differently for different modes while the protein motion may be similar, or perhaps some vibrations are missed due to this effect. In the sample, the biological water, the water within a few layers of the protein surface, will likely move with the protein, but outside of this region, the bulk water will display a standard relaxation response. Also, the large amount of solvent around the protein has a large impact on the dipole derivative magnitude for the NMA. These will therefore
impact the VDOS and isotropic absorbance and that's why should be studied further to
refine the best approach for simulating the physical system.


## Methods of the study:

So for the further refinement, I am studying vibrations of the protein. we determined the conformation of the protein by minimizing the potential energy. At room temperature, although being in its stable position, the protein starts waggling and shows many different configurations. We aim to generate the matrix for each of the configurations within a specific frequency range and correlate the displacement vector with the frequency. So the configurational structure of the protein was chosen randomly during the waggling motion of the protein. The structure was randomly snapped from the video and the matrix for each of those structure needs to be calculated from which we can illustrate the correlation between frequency and eigen vectors.
So I have right now 10 replica structures. Those replica structures are selected randomly during the waggling of the protein. Within each replica structures, there are 90 starting structures i.e altogether there are 900 starting structures.
The absorbtion vs frequency graph of the CEWL protein after NMEA is given below:

![Absorption Vs Frequency Graph](https://github.com/ubsuny/vibrational-motion-CP2P2024/blob/main/four%20peaks.png)

we are going to analyze the correlated motions for the full data set within a given
specific frequency band of interest. Here we will
determine the regions of motion associated with the resonance most
strongly effected by the hydration
So now, I have calculated the matrices for each of the starting structures for each frequency band and averaged the matrix for each frequency range. After the average the correlation plot will obtained.

| Peaks | Frequency | Chosen Frequency Range |
| -------- | -------- | -------- |
| A | 4.5 | 4-5 |
| B | 23.5 | 22.5-24.5 |
| C | 51.4 | 50.4-52.4 |
|D  | 67 | 66-68 |

```p
import numpy as np
fi1 = open("frame_s.asc",'r')
lines1 = fi1.readlines()
band_low = 0.66   ##### set lower boundary
band_up = 0.68  #### set upper #boundary
nol_low = -1   #### find the line in input which represents the lower bdr
nol_up = -1   ###                                               upper bdr
for i in range(len(lines1)):
    line = lines1[i]      
    freq_cur = line.split()[0]
    freq_cur = float(freq_cur)
    if (freq_cur > band_low) and (nol_low == -1):
        nol_low = i       
    if (freq_cur > band_up) and (nol_up == -1):
        nol_up = i - 1    
        break             
print(nol_low)            
print(nol_up) 
a=np.load("frame_U.npz")
Mat=a['arr_0']
#Mat = np.loadtxt("frame_U.asc")
disp = []                 
for i in range(nol_up-nol_low+1):
    disp.append([])       
pdb = open("deleted.pdb", 'r')
pdblines = pdb.readlines()
for line in pdblines:     
    words = str.split(line)
    if len(words) < 1:    
        pass
    elif words[0] == "ATOM":
        atomname = line[13:16].strip()
        if atomname == "CA":
            resid = line[22:26].strip()
            atomnumber = line[5:11].strip()
            for j in range(nol_up - nol_low + 1):
                disp[j].append([Mat[int(atomnumber) * 3 -3, j + nol_low], Mat[int(atomnumber) * 3 - 2, j + nol_low], Mat[int(atomnumber) * 3 - 1, j + nol_low]])
corre = np.zeros((nol_up-nol_low+1, len(disp[0]), len(disp[0])))
for i in range(nol_up-nol_low+1):
    for j in range(len(disp[0])):
        for k in range(len(disp[0])):
            corre[i, j, k] = np.dot(disp[i][j],disp[i][k])
np.save("correlation_66to68.npy",corre)
```
```p
#!/bin/env python

import sys
import numpy as np
import math

#use_standard_error = True

#def matrixToSplot(fname, A, factor=15.0):
#    (m, n) = A.shape
#    fout = open(fname, 'w')
#    for j in range(m):
#        frequency = A[j][0]
#        for i in range(1, n):
#            line = "%f\t%f\t%f\n" % ( ((i-1)*factor), frequency, A[j][i])
#            fout.write(line)
#        fout.write('\n')
#    fout.close()




prefix = sys.argv[1]
filenames = open(sys.argv[2],'r')
lines = filenames.readlines()
matrices = []

for filename in lines:
    A = np.load(filename[:-1])
    avg = np.mean(A, axis = 0)
    matrices.append(avg)

avg = np.mean(matrices, axis=0)
#std = np.std(matrices, axis=0)
#if use_standard_error:
#    std /= math.sqrt(len(matrices))
#std[:,0] = avg[:,0]
#avg = avg/np.amax(avg)
np.savetxt(prefix + '_avg.asc', avg)
#matrixToSplot(prefix + '_avg_plot.asc', avg)

#np.savetxt(prefix + '_std.asc', std)
#matrixToSplot(prefix + '_std_plot.asc', std)
```


![Plot for peak 1](https://github.com/ubsuny/vibrational-motion-CP2P2024/blob/main/average%20plot%20for%20frequency%20range%204to5.png)

![Plot for peak 2](https://github.com/ubsuny/vibrational-motion-CP2P2024/blob/main/average%20plot%20for%20frequency%20range%2022.5%20to%2024.5.png)

![Plot for peak 3](https://github.com/ubsuny/vibrational-motion-CP2P2024/blob/main/average%20plot%20for%20the%20frequency%20range%2050.4%20to%2052.4.png)

![Plot for peak 4](https://github.com/ubsuny/vibrational-motion-CP2P2024/blob/main/average%20plot%20for%20the%20frequency%20range%2066%20to%2068.png)


# Disscussion of the graph not done yet. Also need to do the same calculation using principal component analysis.




