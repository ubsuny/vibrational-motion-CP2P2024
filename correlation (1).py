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
