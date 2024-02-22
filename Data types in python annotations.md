# Data Types
### As I will be working on the vibrational motion of the protein, my input data has the values of eigenvectors ( displacement of the protein atoms due to vibration) at certain eigenvalues (frequencies). The input data are in scientific notation and represent decimal number, so data types of my project is floating point number i.e. 'float64'.

![First 10 rows and columns of the data](https://github.com/ubsuny/vibrational-motion-CP2P2024/blob/main/Data%20type.png)

### Python Annotation:

```python

import numpy as np

def analyze_vibrations(eigenvalues: np.ndarray, eigenvectors: np.ndarray) -> None:
    """
    Analyze the vibrations of a protein given its eigenvalues (frequencies) and eigenvectors (displacements).
    
    Parameters:
        eigenvalues (np.ndarray): An array of floating-point numbers representing the frequencies of the vibrations.
        eigenvectors (np.ndarray): An array of floating-point numbers representing the displacements
            due to vibrations. Each column corresponds to an eigenvector.
    
    Returns:
        None
    """
   ```


