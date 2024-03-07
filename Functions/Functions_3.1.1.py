##################################################
# Fonsiyonlar, Koşullar, Döngüler, Comprehensions
##################################################

# - Fonksiyonlar (Functions)
# - Koşullar (Conditions)
# - Döngüler (Loops)
# - Comprehesions

################################
# Fonksiyonlar (Functıons)
################################

################################
# Fonksiyon Okuryazarlığı
################################

# Bir fonksiyonun içeriğini öğrenmöek için help(fonksiyon adı) yazılır terminale

print("merhaba")
print("merhaba", "fatih")
print("merhaba", "fatih", sep="__")


################################
# Fonksiyon Tanımlama
################################

def calculate(x):
    print(x*2)


calculate(10)


# İki argümanlı/parametreli bir tanıyalım.

def summer(arg1, arg2):
    print(arg1+arg2)


summer(10, 20)
