################################
# Fonksiyonların Statement/Body Bölümü
################################

# def function_name(parameters/arguments):
#    statements (funvtion body)

def say_hi():
    print("hello")
    print("hi")
    print("merhaba")


say_hi()


def say_hi(string):
    print(string)
    print("hi")
    print("merhaba")


say_hi("fatih")


def multiplication(a, b):
    c = a * b
    print(c)


multiplication(10, 9)

# girilen değerleri bir liste içinde saklayacak fonksiyon.

list_store = []


def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)


add_element(1, 8)
add_element(180, 66)
