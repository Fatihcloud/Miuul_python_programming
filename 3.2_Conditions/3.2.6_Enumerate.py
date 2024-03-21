################################
# Enumerate: Otomatik counter/indexer ile for loop
################################

students = ["john", "mark", "venessa", "mariam"]

for student in students:
    print(student)

for index, student in enumerate(students):
    print(index, student)

A = []
B = []

for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)
print(A)
print(B)

################################
# Uygulama - Mülakat sorusu
################################
# divide_students fonksiyonu yazınız
# çift indexte yer alan öğrencileri bir listeye alınız
# tek indexte yer alan öğrencileri bir başka bir listeye alınız
# fakat bu iki liste tek bir liste olarak return olsun

students = ["john", "mark", "venessa", "mariam"]


def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups


divide_students(students)


################################
# alternating fonksiyonunun enumerate ile yazılması
################################

def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()

    print(new_string)


alternating_with_enumerate("merhaba")
