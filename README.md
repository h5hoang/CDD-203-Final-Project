# CDD-203-Final-Project: hERG_Karim Drug Classification using an Ensemble Model
hello my name is hanson this is my readme

## Introduction
This project utilizes a Machine Learning model to classify drugs into 2 categories, whether they are a blocker (1) or a non-blocker (0) to the hERG channel. The dataset contains molecular information in the form of SMILES strings, which is used to generate fingerprints for various machine learning models, which their outputs are then fed into an ensemble model for a final prediction. The usage of the ensemble model for this dataset is inspired by the reference paper for this dataset, which can be found in the next section.

## Data
The dataset used in this project is the hERG channel inhibition dataset, retrieved from the Toxicology Data Challenge (TDC). Specifically, we use the "hERG_Karim" dataset from the TDC's single prediction task. The links are attached below along with the reference paper for the dataset:
* [Dataset](https://tdcommons.ai/single_pred_tasks/tox#herg-karim-et-al)
* [Reference Paper](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-021-00541-z)

## Setting Up the Environment
Please make sure that Conda is installed before following the next steps!! 

[Conda Installation Guide](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

Now let's begin:
1. Clone the repository:

        git clone https://github.com/h5hoang/CDD-203-Final-Project
        cd CDD-203-Final-Project
            
2. Create a Conda Environment:
        
        conda create --name ensemble 
        conda activate ensemble

3. Install pip in the Conda Environment:

        conda install pip

4. Head into `packages.py` and run the script using the command:

        python packages.py

   This script will install the following packages:
   * pandas - load, manipulate, clean, and analyze data
   * numpy - performing numerical operations
   * PyTDC - download and access the hERG_Karim dataset
   * rdkit - generate molecular fingerprints from SMILES strings
   * scikit-learn - implement various machine learning algorithms
   * seaborn - creating statistical graphs

* If packages.py fails, you can manually install the packages through the following commands:

        pip install pandas
        pip install numpy
        pip install PyTDC
        pip install rdkit
        pip install scikit-learn 
        pip install seaborn

* <ins>**As an extra precaution, I've also included the pip commands in the first section, "Install Necessary Libraries" in `ensemble_model.ipynb.` Click the run button on the left of the cell in that section and proceed with the rest of the jupyter notebook as usual.** </ins>

## Reproduction of Results
Once the environment has been set up, head into `ensemble_model.ipynb` in this repo. `ensemble_model.ipynb` will contain code that will:

1. Install Necessary Packages if running `packages.py` fails
2. Importing the hERG_Karim dataset
3. Cleaning the hERG_Karim dataset
4. Initialize the Ensemble model with 5 other ML Models:

        * Gradient Boosting 
        * Random Forest
        * Logistic Regression
        * Extra Trees
        * K Neighbors
5. Finetune Parameters for each of the 5 model using RandomizedSearchCV
6. Input RandomizedSearchCV outputted parametersr into the models
7. Run Ensemble model on test dataset
8. Visualization of Ensemble Model Results

Comments are written throughout the jupyter notebook to help aid in the thought process for each step. 

Please let me know if there are questions, concerns, and especially suggestions for this process at hanson.hoang@ucsf.edu!