#########################################################################
# Virtual Environment (Sanal ortam) ve (Package Mangment) Paket Yönetimi
#########################################################################

# Sanal ortamların listelenmesi
# conda env list

# Sanal ortam oluşturma
# conda create -n my_env

# Sanal ortam aktif etme
# conda activate my_env

# Ortam içerisindeki paketler listelenir
# conda list

# Paket yükleme:
# conda install numpy

# Aynı anda birden fazla oaket yükleme:
# conda install numpy scipy pandas

# Paket silme:
# conda remove numpy

# Belirli bir versiyona göre paket yükleme:
# conda install numpy=1.20.1

# Paket yükseltme:
# conda upgrade numpy

# Tüm paketleri yükseltmesi:
# conda upgrade -all

# pip: pypi (python package index) paket yönetimi aracı

# Paket yükleme:
# pip install pandas

# Paket yükleme versiyona göre:
# pip install pandas==2.0.0

# Bir yaml oluşturma:
# conda env export > environment.yaml

# Bir yaml içinden yeniden env oluşturma:
# conda env create -f environment.yaml