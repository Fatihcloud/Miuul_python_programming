################################
# Dict 3.3_Comprehensions
################################

dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}

dictionary.keys()
dictionary.values()
dictionary.items()

{k: v ** 2 for (k, v) in dictionary.items()}

{k.upper(): v for (k, v) in dictionary.items()}

{k.upper(): v * 2 for (k, v) in dictionary.items()}

################################
# Uygulama - Mülakat sorusu
################################

# amaç: çift sayıların karesi alınarak bir sözlüğe eklemek istenmektedir
# key'ler orjinal değerler value'lar ise değiştirilmiş değerler olcak.


numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2
    else:
        new_dict[n] = n

{n ** 2 if n % 2 == 0 else n: n for n in numbers}
