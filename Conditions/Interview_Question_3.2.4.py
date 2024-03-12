################################
# Uygulama - Mülakat Sorusu
################################

# Amaç: aşağıdaki şekilde string deiştiren fonksiyon yazmak istiyoruz

# before: "hi my name is john and i am learning python"
# after: "hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

range(len("miull"))
range(0, 5)

for i in range(len("miull")):
    print(i)


def alternating(string):
    new_string = ""
    for string_index in range(len(string)):  # Girilen string'in index'lerinde gez.
        if string_index % 2 == 0:  # index çift ise büyük harfe çevir.
            new_string += string[string_index].upper()
        else:  # index tek ise küçük harfe çevir.
            new_string += string[string_index].lower()
    print(new_string)


alternating("miuul")
