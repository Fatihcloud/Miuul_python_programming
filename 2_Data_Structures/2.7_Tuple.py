################################
# Demet (Tuple)
################################

# - Değiştirelemez.
# - Sıralıdır.
# - Kapsayıcıdır.

t = ("john", "mark", 1, 3)
type(t)

t[0]
t[0:3]

t[0] = 99

t = list(t)
t[0] = 99
t = tuple(t)
