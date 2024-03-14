################################
# Index seçimi (ındex selection)
################################

import numpy as np

a = np.random.randint(10, size=10)

a[0]
a[0:5]
a[0] = 999

m = np.random.randint(10, size=(3, 5))

m[0, 0]
m[1, 1]
m[2, 3] = 10
m[2, 3] = 101.1 # numpy tek tipte yani int tipinde veri tutar bu yüzden bunu 101 olarak alır.

m[: ,0]
m[1 ,:]
m[0:2 ,0:3]

################################
# Fancy Index
################################

import numpy as np

v = np.arange(0, 30, 3)

catch = [1, 2, 3]
# Birden fazla değeri içinden almak istersek bunun gibi bir liste oluşturuyoruz sonra bunu içine veriyoruz.

v[catch]
