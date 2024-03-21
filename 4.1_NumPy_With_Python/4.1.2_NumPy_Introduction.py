################################
# NUMPY
################################

# Neden NumPy? (Why Numpy?)
# NumPy Array'i Oluşturmak (Creating Numpy Arrays)
# NumPy Array Özellikleri (Attibutes of Numpy Arrays)
# Yeniden Şekillendirme (Reshaping)
# Index Seçimi (Index Selection)
# Slicing
# Fancy Index
# Numpy'da Koşullu İşlemler (3.2_Conditions on Numpy)
# Matematiksel İşlemler (Mathematical Operations)


################################
# klasik yolu
a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

################################
# numpy yolu
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])

a * b

################################
# NumPy Array'i oluşturmak (Creating numpy arrays)
################################

import numpy as np

np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5]))

np.zeros(10, dtype=int)

np.random.randint(0, 10, size=10)

np.random.normal(10, 4, (3, 4))

################################
# NumPy Array Özellikleri (Attibutes of numpy arrays)
################################

import numpy as np

# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

a = np.random.randint(10, size=5)

a.ndim
a.shape
a.size
a.dtype
