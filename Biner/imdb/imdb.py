# ============================================================
# KLASIFIKASI BINER - IMDB Dataset of 50K Movie Reviews
# Sumber (URL) : https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews
# Deskripsi    : 50.000 ulasan film berbentuk teks. Kolom label = 'sentiment':
#                positive atau negative.
#                Jumlah kelas = 2 -> KLASIFIKASI BINER.
# File CSV     : IMDB Dataset.csv  
# ============================================================
import os
import pandas as pd

folder = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(folder, "IMDB Dataset.csv")
if not os.path.exists(path):
    raise SystemExit("File 'IMDB Dataset.csv' belum ada. Download dari link Kaggle di atas, "
                     "lalu taruh di folder: " + folder)

df = pd.read_csv(path)
kolom_label = "sentiment"          # kolom yang menjadi label

print("Sumber       : https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews")
print("Ukuran data  :", df.shape)
print("Kolom label  :", kolom_label)
print("Nama kelas   :", list(df[kolom_label].unique()))
print("Jumlah kelas :", df[kolom_label].nunique())
print("\nJumlah data per kelas:\n", df[kolom_label].value_counts())
print("\nContoh ulasan:\n", df["review"][0][:200], "...")
