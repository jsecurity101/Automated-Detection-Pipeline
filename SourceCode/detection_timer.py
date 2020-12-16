#Author: Jonathan Johnson
import nbformat
import pandas as pd
import os

from nbconvert.preprocessors import ExecutePreprocessor

print("Detection Notebook is running....")
with open('Detection Notebooks/Service Creation (T1543.003)/Service_Creation_Detection.ipynb') as f:
    nb = nbformat.read(f, as_version=4)
ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(nb, {'metadata': {'path': 'Detection Notebooks/Service Creation (T1543.003)'}})
with open('Detection Notebooks/Service Creation (T1543.003)/Service_Creation_Detection.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)
df1 = pd.read_pickle('Base_Condition')
print("Detection Notebook is done running....")
os.remove("Base_Condition")


if len(df1.index) > 0:
    print("Triage Notebook is running....")
    with open('Detection Notebooks/Service Creation (T1543.003)/Service_Creation_Triage.ipynb') as f:
        nb = nbformat.read(f, as_version=4)
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb, {'metadata': {'path': 'Detection Notebooks/Service Creation (T1543.003)'}})
    with open('Detection Notebooks/Service Creation (T1543.003)/Service_Creation_Triage.ipynb', 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    df2 = pd.read_pickle('Final_DF') 
    print("Triage Notebook is done running....")                                
    os.remove("Final_DF")
    
    if len(df2.index) > 0:
        print("Investigation Notebook is running....")
        with open('Detection Notebooks/Service Creation (T1543.003)/Service_Creation_Investigations.ipynb') as f:
            nb = nbformat.read(f, as_version=4)
        ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
        ep.preprocess(nb, {'metadata': {'path': 'Detection Notebooks/Service Creation (T1543.003)'}})
        with open('Detection Notebooks/Service Creation (T1543.003)/Service_Creation_Investigations.ipynb', 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print("Investigation Notebook is done running....")


else:
    print("No Data")
