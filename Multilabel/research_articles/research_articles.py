# ============================================================
# KLASIFIKASI MULTILABEL - Topic Modeling for Research Articles
# Sumber (URL) : https://www.kaggle.com/datasets/vetrirah/janatahack-independence-day-2020-ml-hackathon
#                (kalau link tidak terbuka, cari judul "Topic Modeling for Research Articles" di Kaggle)
# Deskripsi    : ±21.000 judul dan abstrak artikel ilmiah. Tiap artikel punya 6 kolom
#                topik bernilai 0/1: Computer Science, Physics, Mathematics, Statistics,
#                Quantitative Biology, Quantitative Finance.
#                Satu artikel bisa masuk beberapa topik sekaligus -> MULTILABEL.
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

# Cari kolom label. Nama kolom disamakan dulu (huruf kecil, spasi -> garis bawah)
# supaya tetap cocok walaupun penulisannya beda: "Computer Science" / "computer_science".
topik = ["computer_science", "physics", "mathematics", "statistics",
         "quantitative_biology", "quantitative_finance"]
nama_baru = {c: c.strip().lower().replace(" ", "_") for c in df.columns}
df = df.rename(columns=nama_baru)
kolom_label = [c for c in topik if c in df.columns]

if not kolom_label:
    raise SystemExit("Kolom topik tidak ditemukan. Kolom yang ada: " + str(list(df.columns)))

print("Sumber        : https://www.kaggle.com/datasets/vetrirah/janatahack-independence-day-2020-ml-hackathon")
print("Ukuran data   :", df.shape)
print("Kolom label   :", kolom_label)
print("Jumlah label  :", len(kolom_label))
print("\nJumlah data per label:\n", df[kolom_label].sum())
# bukti multilabel: ada artikel yang punya lebih dari 1 topik
print("\nBerapa label dalam 1 artikel:\n", df[kolom_label].sum(axis=1).value_counts().sort_index())
