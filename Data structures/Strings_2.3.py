####################################
# Karakter Dizileri (Strings)
####################################

print("fatih")

name = "melisa"
print(name)

################################
# Çok satırlı karakter dizileri
################################

long_str = """merhaba ben fatih size nasıl yardımcı olabilirim"""

################################
# Karakter Dizlerinin Elemanlarına Erişmek
################################

name = "Fatih"
name[0]

################################
# Karakter Dizlerinin Slice İşlemi
################################

name = "Melisa"
name[0:2]

################################
# String İçerisinde Karakter Sorgulamak
################################

"nasıl" in long_str

################################
# String (Karakter Dizisi) Metodları
################################

dir(str)

################################
# len
################################

name = "fatih"
type(name)
type(len)

len(name)
len("fatih&melisa")

################################
# upper() & lover(): küçük-büyük dönüşümleri
################################

"miuul".upper()
"MIUUL".lower()

################################
# replace: karakter değiştirir
################################

hi = "Fatih merhaba"
hi.replace("a", "o")

################################
# split: böler
################################

"hello fatih naber".split()

################################
# strip: kırpar
################################

" ofofo ".strip()

################################
# capitalize: ilk harfi büyür
################################

"foo".capitalize()
