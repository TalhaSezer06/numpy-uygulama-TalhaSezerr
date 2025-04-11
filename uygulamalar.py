 
# uygulamalar.py

import numpy as np

# NumPy Getting Started
# NumPy kütüphanesini import ederek başlıyoruz.
print("NumPy Başladı!")

# NumPy Creating Arrays
# Listeyi NumPy dizisine çeviriyoruz.
arr1 = np.array([1, 2, 3, 4])
print("Array Oluşturma:", arr1)

# NumPy Array Indexing
# Dizinin belli bir elemanına erişiyoruz.
print("Indexleme - 2. eleman:", arr1[1])

# NumPy Array Slicing
# Diziyi dilimleyerek bir kısmını alıyoruz.
print("Slicing - İlk üç eleman:", arr1[:3])

# NumPy Data Types
# Dizi veri tipini kontrol ediyoruz.
print("Veri Tipi:", arr1.dtype)

# NumPy Copy vs View
# Copy ve View farkını gözlemliyoruz.
copy_arr = arr1.copy()
view_arr = arr1.view()
arr1[0] = 100
print("Copy:", copy_arr)
print("View:", view_arr)

# NumPy Array Shape
# Çok boyutlu dizinin şeklini kontrol ediyoruz.
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Shape (şekil):", arr2d.shape)

# NumPy Array Reshape
# Dizi şeklini değiştiriyoruz.
reshaped = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
print("Reshaped Dizi:\n", reshaped)

# NumPy Array Iterating
# Dizi elemanları üzerinde döngü ile geziniyoruz.
print("Dizi Üzerinde Döngü:")
for x in arr1:
    print(x)

# NumPy Array Join
# İki diziyi birleştiriyoruz.
joined = np.concatenate(([1, 2], [3, 4]))
print("Birleştirme:", joined)

# NumPy Array Split
# Diziyi eşit parçalara bölüyoruz.
split = np.array_split(np.array([1, 2, 3, 4, 5, 6]), 3)
print("Split Sonuçları:")
for parca in split:
    print(parca)

# NumPy Array Search
# Belirli bir değerin indeksini arıyoruz.
search_arr = np.array([4, 5, 6, 7])
index = np.where(search_arr == 6)
print("6 sayısının indeksi:", index)

# NumPy Array Sort
# Dizi elemanlarını sıralıyoruz.
unsorted = np.array([3, 1, 4, 2])
sorted_arr = np.sort(unsorted)
print("Sıralanmış:", sorted_arr)

# NumPy Array Filter
# Belirli koşulu sağlayan elemanları filtreliyoruz.
filter_arr = np.array([10, 15, 20, 25])
filtre = filter_arr[filter_arr > 15]
print("15'ten büyükler:", filtre)
