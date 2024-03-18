################################
# Veri okuma (Reading Data)
################################

import pandas as pd

df = pd.read_csv("Datasets/Advertising.csv")
df.head()

################################
# Veriye Hızlı Bakış (Quick Look at Data)
################################

import seaborn as sns

df = sns.load_dataset("titanic")
df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T()
df.isnull().values.any()
df.isnull().sum()
df["sex"].value_counts()