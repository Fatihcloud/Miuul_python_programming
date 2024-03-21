################################
# List & Dict 3.3_Comprehensions Applications
################################


################################
# Bir veri setindeki değişken isimlerini değiştirmek
################################

# before:
# ['total', 'speeding', 'alcohol']

# after:
# ['TOTAL', 'SPEEDING', 'ALCOHOL']


import seaborn as sns
df = sns.load_dataset('car_crashes')
df.columns

for col in df.columns:
    print(col.upper())

a = []

for col in df.columns:
    a.append(col.upper())

df.columns = a

# Yeni yöntem ile nasıl yapılır

df = sns.load_dataset('car_crashes')

df.columns = [col.upper() for col in df.columns]

################################
# İsminde "INS" olan değişkenlerin başına FLAG diğerlerine NO_FLAG eklemek istiyoruz.
################################

[col for col in df.columns if "INS" in col]

["FLAG_" + col for col in df.columns if "INS" in col]

["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

################################
# Amaç key'i string, value'su aşağıdaki gibi liste olan sözlük oluşturmak.
################################

import seaborn as sns
df = sns.load_dataset('car_crashes')
df.columns

num_cols = [col for col in df.columns if df[col].dtype != "O"]

soz = {}
agg_list = ["mean", "min", "max", "sum"]

for col in num_cols:
    soz[col] = agg_list

# Kısa yol
new_dict = {col: agg_list for col in num_cols}

df[num_cols].head()

df[num_cols].agg(new_dict)
