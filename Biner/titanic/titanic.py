# ============================================================
# KLASIFIKASI BINER - Titanic
# Sumber (URL) : https://www.kaggle.com/c/titanic/data
# Deskripsi    : Data penumpang kapal Titanic (891 baris): usia, kelas tiket,
#                jenis kelamin, dll. Kolom label = 'Survived':
#                0 = tidak selamat, 1 = selamat.
#                Jumlah kelas = 2 -> KLASIFIKASI BINER.
# File CSV     : train.csv  
# ============================================================
import os
import pandas as pd

folder = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(folder, "train.csv")
if not os.path.exists(path):
    raise SystemExit("File train.csv belum ada. Download dari link Kaggle di atas, "
                     "lalu taruh di folder: " + folder)

df = pd.read_csv(path)
kolom_label = "Survived"           # kolom yang menjadi label

print("Sumber       : https://www.kaggle.com/c/titanic/data")
print("Ukuran data  :", df.shape)
print("Kolom label  :", kolom_label)
print("Nama kelas   :", sorted(df[kolom_label].unique()), "(0 = tidak selamat, 1 = selamat)")
print("Jumlah kelas :", df[kolom_label].nunique())
print("\nJumlah data per kelas:\n", df[kolom_label].value_counts())
print("\nContoh data:\n", df.head())
