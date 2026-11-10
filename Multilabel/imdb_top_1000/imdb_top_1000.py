# ============================================================
# KLASIFIKASI MULTILABEL - IMDB Top 1000 Movies and TV Shows
# Sumber (URL) : https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows
# Deskripsi    : 1.000 film/serial terbaik di IMDB. Kolom label = 'Genre' berisi
#                maksimal 3 genre dipisah koma, contoh "Drama, Crime".
#                Satu film bisa punya beberapa genre sekaligus -> MULTILABEL.
# File CSV     : imdb_top_1000.csv  
# ============================================================
import os
import pandas as pd

folder = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(folder, "imdb_top_1000.csv")
if not os.path.exists(path):
    raise SystemExit("File imdb_top_1000.csv belum ada. Download dari link Kaggle di atas, "
                     "lalu taruh di folder: " + folder)

df = pd.read_csv(path)

# cari kolom genre (huruf besar/kecil tidak masalah)
kolom_label = None
for c in df.columns:
    if c.strip().lower() in ("genre", "genres"):
        kolom_label = c
if kolom_label is None:
    raise SystemExit("Kolom genre tidak ditemukan. Kolom yang ada: " + str(list(df.columns)))

# ubah teks "Drama, Crime" menjadi tabel 0/1 (satu kolom per genre)
y = df[kolom_label].str.get_dummies(sep=", ")

print("Sumber        : https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows")
print("Ukuran data   :", df.shape)
print("Kolom label   :", kolom_label)
print("Jumlah label (genre unik):", y.shape[1])
print("\nJumlah data per label:\n", y.sum().sort_values(ascending=False))
# bukti multilabel: 1 film bisa punya lebih dari 1 genre
print("\nBerapa label dalam 1 film:\n", y.sum(axis=1).value_counts().sort_index())
