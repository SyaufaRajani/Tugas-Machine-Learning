# ============================================================
# KLASIFIKASI BINER - Breast Cancer Wisconsin (Diagnostic)
# Sumber (URL) : https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data
# Deskripsi    : Data hasil citra sel tumor payudara (569 baris, 30 fitur numerik).
#                Kolom label = 'diagnosis': M = malignant (ganas), B = benign (jinak).
#                Jumlah kelas = 2, tiap data punya 1 label -> KLASIFIKASI BINER.
# File CSV     : data.csv  
# ============================================================
import os
import pandas as pd

folder = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(folder, "data.csv")
if not os.path.exists(path):
    raise SystemExit("File data.csv belum ada. Download dari link Kaggle di atas, "
                     "lalu taruh di folder: " + folder)

df = pd.read_csv(path)
kolom_label = "diagnosis"          # kolom yang menjadi label

print("Sumber       : https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data")
print("Ukuran data  :", df.shape)
print("Kolom label  :", kolom_label)
print("Nama kelas   :", list(df[kolom_label].unique()), "(M = ganas, B = jinak)")
print("Jumlah kelas :", df[kolom_label].nunique())
print("\nJumlah data per kelas:\n", df[kolom_label].value_counts())
print("\nContoh data:\n", df.head())
