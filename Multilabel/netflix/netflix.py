# ============================================================
# KLASIFIKASI MULTILABEL - Netflix Movies and TV Shows
# Sumber (URL) : https://www.kaggle.com/datasets/shivamb/netflix-shows
# Deskripsi    : ±8.800 judul film/serial Netflix. Kolom label = 'listed_in'
#                berisi beberapa genre dipisah koma, contoh "Dramas, International Movies".
#                Satu judul bisa punya beberapa genre sekaligus -> MULTILABEL.
# File CSV     : netflix_titles.csv  
# ============================================================
import os
import pandas as pd

folder = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(folder, "netflix_titles.csv")
if not os.path.exists(path):
    raise SystemExit("File netflix_titles.csv belum ada. Download dari link Kaggle di atas, "
                     "lalu taruh di folder: " + folder)

df = pd.read_csv(path)
kolom_label = "listed_in"          # kolom yang menjadi label (berisi banyak genre)

# ubah teks "A, B, C" menjadi tabel 0/1 (satu kolom per genre)
y = df[kolom_label].str.get_dummies(sep=", ")

print("Sumber        : https://www.kaggle.com/datasets/shivamb/netflix-shows")
print("Ukuran data   :", df.shape)
print("Kolom label   :", kolom_label)
print("Jumlah label (genre unik):", y.shape[1])
print("\n10 label terbanyak:\n", y.sum().sort_values(ascending=False).head(10))
# bukti multilabel: 1 judul bisa punya lebih dari 1 genre
print("\nBerapa label dalam 1 judul:\n", y.sum(axis=1).value_counts().sort_index())
