import pandas as pd

# Veriyi oku
df = pd.read_csv("sample_data.csv")

# İlk hali
print("Orijinal Veri:")
print(df.head())

# Boş değerleri temizle
df_cleaned = df.dropna()

# Yinelenenleri temizle
df_cleaned = df_cleaned.drop_duplicates()

# Kolon isimlerini düzelt
df_cleaned.columns = [col.strip().lower().replace(" ", "_") for col in df_cleaned.columns]

# Temizlenmiş veriyi kaydet
df_cleaned.to_csv("cleaned_data.csv", index=False)

print("\nTemizlenmiş veri 'cleaned_data.csv' dosyasına kaydedildi.")
