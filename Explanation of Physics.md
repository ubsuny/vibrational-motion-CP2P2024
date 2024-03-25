
# Explanation of Physics

The protein dynamics studied in this work were performed on the enzymatic protein lysozyme, specifically the variety found in chicken egg whites (CEWL). A single protein can have several different configurations: unfolded, folded, and partially folded. Many proteins have rigid structures, and deviate only in small fluctuations from the natural folded structure, while others can undergo large conformational changes due to binding, charge transfer, or the surrounding environment. These fluctuations and conformational changes have been shown to be functionally relevant [^1].

The most probable structure of protein is frequently the most energetically favorable, i.e. the lowest energy. A protein’s structure is able to fluctuate. It is not as rigidly defined as a crystal object, allowing for both large and small fluctuations relative to the protein size. When proteins are frozen, the thermal energy is much lower which will cause the the protein to move toward one of the energy minima. However, at non-zero temperatures, the protein can still move in the energy landscape. This results in an ensemble of possible folded states, the distribution of which varies for each type of protein [^2].

![Absorption Vs Frequency Graph](https://github.com/ubsuny/vibrational-motion-CP2P2024/blob/main/Screenshot%20(98).png)


If the energy landscape is known, one can use it to calculate protein vibrations. In normal mode analysis (NMA) the protein vibrations are approximated to be harmonic around the protein’s energy minimized structure. This approximation can be useful in obtaining some of the protein vibrational motions, however, the harmonic approximation will not include the anharmonic contributions.




### Normal Mode Analysis
Normal mode analysis (NMA) is a computational technique widely employed in structural biology, computational chemistry, and materials science to investigate the vibrational motions and dynamics of molecules and molecular complexes. NMA involves calculating the normal modes of a system, which represent the collective vibrational motions. Each normal mode is characterized by its frequency and associated vibrational pattern, depicting how atoms move relative to each other. In applications, NMA proves invaluable: in structural biology, it elucidates protein dynamics, including conformational changes and flexibility; in computational chemistry, it predicts vibrational spectra and analyzes molecular dynamics. 

### Normal Mode Ensemble Analysis
The NMA method is most appropriate for modeling frozen samples, in which the structure is fairly ridged. At higher temperature the protein structure may occupy multiple conformations or move between structures due to the thermal energy. Each of these different structures each potentially have a different set of vibrational modes, due to the varying structures. Since the measurements  were performed at room temperature, and the samples contain a large concentration of proteins, it is necessary to include multiple protein conformations in the calculations. 

In order to account for this variation in the protein configurations within the sample and the resulting impact on potential vibrations, we introduce Normal Mode Ensemble Analysis (NMEA). In this method, multiple protein structures from the same MD simulation are obtained and each is minimized to the same average energy gradient tolerance. Normal mode analysis is performed on each minimized structure to obtain the vibrational mode frequencies, displacement vectors, and dipole derivative vectors. These are used to calculate the desired
information from each set of NMA results separately, such as vibrational density of states, isotropic absorbance, and anisotropic absorbance (the calculations of which are described in later sections). The individual calculated spectra are then averaged to provide the ensemble results.

### Vibrational Motions of protein and relation to function:
When all of the atoms in the system move in a correlated fashion at a specific vibrational frequency, the motions are referred to as vibrational modes. In a physical system at non-zero temperatures, the protein motion is a superposition of vibrational modes and local vibrations. One such example of the relation of protein motions and function is through binding. Many proteins undergo conformational changes upon binding. Two major models have been proposed for the binding of a protein and substrate (which could be a
ligand, small molecule, or another protein): 1) the induced fit model and 2) conformational selection model. The induced fit model describes a process in which the protein conformation is fixed until the substrate causes a change in the protein structure through interactions to facilitate binding. The conformational selection model describes a system in which the protein moves in dynamic equilibrium, whose conformations include both the free and bound structures, the substrate will bind to and stabilize the preferred conformation [^3].

## Necessity of this study:

![Absorption Vs Frequency Graph](https://github.com/ubsuny/vibrational-motion-CP2P2024/blob/main/Screenshot%20(99).png)

Figure shows a comparison of the results obtained for free WT CEWL. The QHA and NMA was performed after MD simulation. The NMA was performed  with the inclusion of the neutralizing ions and 7 A water layer. The VDOS in Fig shows that the ˚VDOS is slightly higher for the QHA results below 20 cm<sup>-1</sup>. Above 20 cm<sup>-1</sup> the VDOS is much higher for the NMA calculated modes, which peaks around 70 cm<sup>-1</sup>. The QHA consistently provides lower frequency modes than the NMA results. The trend of the VDOS spectrum is opposite for the isotropic absorbance spectra. It can be seen that the dipole derivative magnitude fluctuates for each mode, however, the average magnitude is higher for the QHA modes. The shape of the isotropic absorbance spectrum from QHA is different than those calculated using NMA. The isotropic absorbance from the QHA peaks around 6 cm<sup>-1</sup> and gradually decreases with increasing frequency, whereas for the NMA results the spectrum gradually increases until around 60 cm<sup>-1</sup> then levels off. 

While the MD simulation used to determine the QHA modes contains solvent, only the protein motions are considered when performing the calculation. However, NMA includes the motions of the solvent in the calculation. Therefore for all calculated modes, the solvent around the protein moves in concert with the protein motion. This may lead to a double counting of some protein motions in which the solvent moves differently for different modes while the protein motion may be similar, or perhaps some vibrations are missed due to this effect. In the sample, the biological water, the water within a few layers of the protein surface, will likely move with the protein, but outside of this region, the bulk water will display a standard relaxation response. Also, the large amount of solvent around the protein has a large impact on the dipole derivative magnitude for the NMA. These will therefore
impact the VDOS and isotropic absorbance and that's why should be studied further to
refine the best approach for simulating the physical system.


## Methods of the study:

So for the further refinement, I am studying vibrations of the protein. we determined the conformation of the protein by minimizing the potential energy. At room temperature, although being in its stable position, the protein starts waggling and shows many different configurations. The configurational structure of the protein was chosen randomly during the waggling motion of the protein. The structure was randomly snapped from the video and the matrix for each of those structure needs to be calculated from which we can illustrate the correlation between frequency and eigen vectors. We aim to generate the matrix for each of the configurations within a specific frequency range and correlate the displacement vector with the frequency.

So I have right now 10 replica structures. Those replica structures are selected randomly during the waggling of the protein. Within each replica structures, there are 90 starting structures i.e altogether there are 900 starting structures (900 modes).
The absorbtion vs frequency graph of the CEWL protein after NMEA is given below:

![Absorption Vs Frequency Graph](https://github.com/ubsuny/vibrational-motion-CP2P2024/blob/main/four%20peaks.png)

we are going to analyze the correlated motions for the full data set within a given specific frequency band of interest. Here we will
determine the regions of motion associated with the resonance most strongly effected by the hydration
So now, I have calculated the matrices for each of the starting structures for each frequency band and averaged the matrix for each frequency range by using below mentioned code. After the average the correlation plot was obtained (plot is at the end).

DISCUSSION OF THE RESULTS TO BE CONTINUED.

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



### References:
[^1]: [Uversky VN. Under-folded proteins: Conformational ensembles and their roles in protein folding, function, and pathogenesis. Biopolymers. 2013 Nov;99(11):870-87. doi: 10.1002/bip.22298. PMID: 23754493; PMCID: PMC7161862.]
[^2]:[ https://www.ncbi.nlm.nih.gov/books/NBK26830/]
[^3]: [Silva DA, Bowman GR, Sosa-Peinado A, Huang X. A role for both conformational selection and induced fit in ligand binding by the LAO protein. PLoS Comput Biol. 2011 May;7(5):e1002054. doi: 10.1371/journal.pcbi.1002054. Epub 2011 May 26. PMID: 21637799; PMCID: PMC3102756.]


#  Also need to do the same calculation for the result of principal component analysis. May be there I can use machine learning.




