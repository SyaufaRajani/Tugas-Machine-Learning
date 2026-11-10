# ============================================================
# KLASIFIKASI MULTIKELAS - MNIST (format CSV)
# Sumber (URL) : https://www.kaggle.com/datasets/oddrationale/mnist-in-csv
# Deskripsi    : 60.000 citra latih digit tulisan tangan 28x28 piksel
#                (784 kolom piksel). Kolom label = 'label': angka 0-9.
#                Jumlah kelas = 10, tiap data punya 1 label -> MULTIKELAS.
# File CSV     : mnist_train.csv  
# ============================================================
import os
import pandas as pd

folder = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(folder, "mnist_train.csv")
if not os.path.exists(path):
    raise SystemExit("File mnist_train.csv belum ada. Download dari link Kaggle di atas, "
                     "lalu taruh di folder: " + folder)

df = pd.read_csv(path)
kolom_label = "label"              # kolom yang menjadi label

print("Sumber       : https://www.kaggle.com/datasets/oddrationale/mnist-in-csv")
print("Ukuran data  :", df.shape, "(1 kolom label + 784 kolom piksel)")
print("Kolom label  :", kolom_label)
print("Nama kelas   :", sorted(df[kolom_label].unique()))
print("Jumlah kelas :", df[kolom_label].nunique())
print("\nJumlah data per kelas:\n", df[kolom_label].value_counts().sort_index())
