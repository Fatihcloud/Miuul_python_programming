################################
# Return: Fonksiyon Çıktılarını girdi olarak kullanmak
################################

def calculate(varm, mositure, charge):
    print((varm + mositure) / charge)


# calculate(34, 56, 87)

def calculate(varm, mositure, charge):
    return (varm + mositure) / charge


calculate(34, 56, 87) * 10

a = calculate(34, 56, 87) * 10


def calculate(varm, mositure, charge):
    varm = varm * 2
    mositure = mositure * 2
    charge = charge * 2
    output = (varm + mositure) / charge
    return varm, mositure, charge, output


calculate(12, 34, 56)

type(calculate(12, 34, 56))

varm, mositure, charge, output = calculate(12, 34, 56)
