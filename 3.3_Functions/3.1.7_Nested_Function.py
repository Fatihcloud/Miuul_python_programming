################################
# Fonksiyon içerisinden fonksiyon çağırmak
################################

def calculate(varm, mositure, charge):
    return int((varm + mositure) / charge)


calculate(100, 100, 1) * 10


def standardization(a, p):
    return a * 10 / 100 * p * p


standardization(45, 1)


def all_calculation(varm, mositure, charge, p):
    a = calculate(varm, mositure, charge)
    b = standardization(a, p)
    print(b * 10)


all_calculation(100, 100, 5, 56)

################################
# Local ve Global Değişkenler (Local & Global Variables)
################################

list_store = [1, 2]  # -> burası global değişken


def add_element(a, b):
    c = a * b  # -> burası local değişken
    list_store.append(c)  # -> local etki alanından global etki alanını etkiliyoruz.
    print(list_store)


add_element(1, 4)
