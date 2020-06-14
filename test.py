# Import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import datadotworld as dw

# Set style & figures inline
sns.set()
# %matplotlib inline

st.write("""
# Testing
Does this work?
""")

# Importando dados do site
#data = pd.read_csv('https://brasil.io/dataset/covid19/caso?format=csv')
data = dw.load_dataset('fehann/brasil-io-covid19')

st.dataframe(data)



pipenv install streamlit numpy pandas matplotlib seaborn datadotworld altair datetime 'click==7.1.2'
