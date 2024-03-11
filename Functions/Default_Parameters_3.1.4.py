################################
# Ön tanımlı argümanlar/parametreler (default parameters(arguments)
################################

def divide(a, b):
    print(a / b)


divide(1, 2)


def divide(a, b=1):
    print(a / b)


divide(1)

################################
# Ne zaman Fonksiyon yazma ihtiyacımız olur?
################################


# varm, moisture, charge

(56 + 25) / 80
(56 + 564) / 33
(45 + 25) / 88


# DRY
def calculate(varm, mositure, charge):
    print((varm + mositure) / charge)


calculate(34, 56, 87)
