import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#thre = 0.035
A = np.loadtxt("Avg5to15matrix_avg.asc")
#m,n = A.shape
#for i in range(m):
#    A[i,i] = 0
#    for j in range(-12, 12):
#      if i + j < m and i + j >=0:
#          A[i+j,i] = 0
#A = A/np.amax(abs(A))
A = A/0.000005
#A = np.mean(A,axis=0)
#A [ abs(A) < thre] = 0
np.savetxt("plotavg_correlation_5to15_run00.asc",A)
B = sns.heatmap(A,cmap = "coolwarm", vmin=-0.15, vmax=0.15)
plt.xlabel("resid")
plt.ylabel("resid")
plt.title("Apo correlation")
plt.show()
