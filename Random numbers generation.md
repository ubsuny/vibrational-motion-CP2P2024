# Random Numbers in My Project

My project is to determine the frequency dependence of the average root mean squared displacements of the waters in the calculations of the vibrations of the hydrated proteins. In my data set, I have the frequencies in the columns and eigenvectors associated with the frequencies in the rows. So I need to find the RMSD from the given data points. I am using machine learning for the findings. So I will be generating training and testing data sets randomly. I will train 80% of the data set and the rest 20% data will be tested using the train_test_split function from sklearn.model_selection.


### Randomness in Data Splitting:

When splitting the data into training and testing sets (or for cross-validation), the train_test_split function from sklearn.model_selection randomly shuffles the data before splitting.
This random shuffling ensures that the data points are randomly distributed between the training and testing sets, reducing the risk of introducing biases in the model evaluation process.

### Randomness while taking snapshot of the video.
As I am studying vibrations of the protein, we determined the conformation of the protein by minimizing the potential energy. At room temperature, although being in its stable position, the protein starts waggling and shows many different configurations. We aim to generate the matrix for each of the configurations within a specific frequency range. So the configurational structure of the protein was chosen randomly during the waggling motion of the protein. The structure was randomly snapped from the video and the matrix for each of those structure needs to be calculated from which we can illustrate the correlation of frequency and other proteins character.


    
   



