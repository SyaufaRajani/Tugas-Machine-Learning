# ============================================================
# KLASIFIKASI MULTIKELAS - Palmer Penguins
# Sumber (URL) : https://www.kaggle.com/datasets/parulpandey/palmer-archipelago-antarctica-penguin-data
# Deskripsi    : Data ±344 penguin (panjang paruh, panjang sirip, berat badan, dll).
#                Kolom label = 'species': Adelie, Chinstrap, Gentoo.
#                Jumlah kelas = 3, tiap data punya 1 label -> MULTIKELAS.
# File CSV     : penguins_size.csv  
# ============================================================
import os
import pandas as pd

folder = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(folder, "penguins_size.csv")
if not os.path.exists(path):
    raise SystemExit("File penguins_size.csv belum ada. Download dari link Kaggle di atas, "
                     "lalu taruh di folder: " + folder)

df = pd.read_csv(path)
kolom_label = "species"            # kolom yang menjadi label

print("Sumber       : https://www.kaggle.com/datasets/parulpandey/palmer-archipelago-antarctica-penguin-data")
print("Ukuran data  :", df.shape)
print("Kolom label  :", kolom_label)
print("Nama kelas   :", list(df[kolom_label].unique()))
print("Jumlah kelas :", df[kolom_label].nunique())
print("\nJumlah data per kelas:\n", df[kolom_label].value_counts())
print("\nContoh data:\n", df.head())
