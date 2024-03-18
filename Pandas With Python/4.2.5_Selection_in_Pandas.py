################################
# Pandas'ta seçim işlemleri (Pandas Selection Procedures)
################################

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()

df.index
df[0:13]
df.drop(0,axis=0).head()

delete_indexes = [1, 3, 5, 7]

df.drop(delete_indexes,axis=0).head()

# df = df.drop(delete_indexes, axis = 0)
# df.drop(delete_indexes, axis = 0, inplace=True)

################################
# Değişkeni Indexe Çevirmek
################################

df["age"].head()
df.age.head()

df.index = df["age"]

df.drop("age", axis=1).head()
df.drop("age", axis=1,inplace=True)
df.head()

################################
# Indexi Değişkene Çevirmek
################################

df.index

df["age"] = df.index
df.drop("age", axis=1,inplace=True)

df.reset_index().head()

################################
# Değişkenler üzerinde işlemler
################################

import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

"age" in df

df["age"].head()
df.age.head()

df["age"].head()
type(df["age"].head())
# <class 'pandas.core.series.Series'> oandas olarak verdi tipini
type(df[["age"]].head())
# <class 'pandas.core.frame.DataFrame'> age iki köşeli parantez kullanarak aldım datafarame olarak verdi

df[["age", "alive"]]

col_names = ["age", "alive", "alone"]

df[col_names].head()

df["age2"] = df["age"]**2
df["age3"] = df["age"] / df["age2"]


df.drop("age3", axis=1).head()

df.drop(col_names, axis=1).head()

df.loc[:, ~df.columns.str.contains("age")].head()
