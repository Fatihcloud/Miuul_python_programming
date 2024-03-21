################################
# Sözlük (Dictonaty)
################################

# Değiştirilebilir
# Sırasızdır.
# Kapsayıcıdır.

# key-value

dictionary = {"REG": "Regression",
              "LOG": "Logistic Regression",
              "CART": "Classification and Reg"}

dictionary["REG"]


dictionary = {"REG": ["RMSE", 10],
              "LOG": ["MSE", 20],
              "CART": ["SSE", 30]}

dictionary["CART"]
dictionary["CART"][1]

################################
# Key Sorgulama
################################

"REG" in dictionary


################################
# Key'e Göre Value'ya Erişmek
################################

dictionary["REG"]
dictionary.get("REG")

################################
# Value Değiştirmek
################################

dictionary["REG"] = ["YSA", 10]


################################
# Tüm Key'lere Erişmek
################################

dictionary.keys()

################################
# Tüm Value'lara Erişmek
################################

dictionary.values()

################################
# Tüm Çiftleri Tuple Halinde Listeye Çevirme
################################

dictionary.items()

################################
# Key-Value Değerlerini Güncellemek
################################

dictionary.update({"REG": 11})

################################
# Yeni Key-Value Değerlerini Ekleme
################################

dictionary.update({"FB": 66})
