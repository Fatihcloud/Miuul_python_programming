################################
# Liste (List)
################################

# - Değiştirilebilir
# - Sıralıdır. Index işlemleri yapılabilir.
# - Kapsayıcıdır

notes = [1, 2, 3, 4]
type(notes)

names = ["a", "b", "v", "d"]

not_nam = [1, 2, "b", "v", 3, 4, True, [1, 2, 3, 4]]

not_nam[0]
not_nam[6]
not_nam[7]
not_nam[7][1]


type(not_nam[7])

type(not_nam[7][1])

################################
# Liste Metodları (List Methods)
################################

dir(notes)

################################
# Len: builtin python fonksiyonu, boyut bilgisi
################################

len(notes)
len(not_nam)

################################
# append: eleman ekler
################################

notes
notes.append(100)

################################
# pop: indexe göre siler
################################

notes.pop(0)

################################
# insert: indexe ekler
################################

notes.insert(0, 88)

