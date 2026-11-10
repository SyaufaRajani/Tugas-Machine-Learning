# ============================================================
# KLASIFIKASI MULTIKELAS - Iris
# Sumber (URL) : https://www.kaggle.com/datasets/uciml/iris
# Deskripsi    : 150 bunga iris dengan 4 fitur (panjang/lebar sepal dan petal).
#                Kolom label = 'Species': Iris-setosa, Iris-versicolor, Iris-virginica.
#                Jumlah kelas = 3, tiap data punya 1 label -> MULTIKELAS.
# File CSV     : Iris.csv  
# ============================================================
import os
import pandas as pd

folder = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(folder, "Iris.csv")
if not os.path.exists(path):
    raise SystemExit("File Iris.csv belum ada. Download dari link Kaggle di atas, "
                     "lalu taruh di folder: " + folder)

df = pd.read_csv(path)
kolom_label = "Species"            # kolom yang menjadi label

print("Sumber       : https://www.kaggle.com/datasets/uciml/iris")
print("Ukuran data  :", df.shape)
print("Kolom label  :", kolom_label)
print("Nama kelas   :", list(df[kolom_label].unique()))
print("Jumlah kelas :", df[kolom_label].nunique())
print("\nJumlah data per kelas:\n", df[kolom_label].value_counts())
print("\nContoh data:\n", df.head())
