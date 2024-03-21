################################
# Numpy'da Koşullu İşlemler (3.2_Conditions on numpy)
################################

import numpy as np

v = np.array([1, 2, 3, 4, 5])

################################
# Klasik döngü ile
################################
ab = []
for i in v:
    if i < 3:
        ab.append(i)

################################
# Numpy döngü ile
################################
v<3
# array([ True,  True, False, False, False])

v[v<3]
# array([1, 2])
