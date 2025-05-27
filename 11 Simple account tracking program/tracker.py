import csv
import os

FILE_NAME = "transactions.csv"

def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Tarih", "Kategori", "Açıklama", "Tutar"])
        print("Yeni işlem dosyası oluşturuldu.")

def add_transaction(date, category, description, amount):
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    print("İşlem başarıyla eklendi.")

def view_transactions():
    if not os.path.exists(FILE_NAME):
        print("Henüz işlem kaydı bulunmamaktadır.")
        return
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print("\t".join(row))

def main():
    create_file()
    print("📊 Basit Hesap Takip Programı")

    while True:
        print("\n1. İşlem Ekle")
        print("2. İşlemleri Görüntüle")
        print("3. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            date = input("Tarih (GG/AA/YYYY): ")
            category = input("Kategori (Gelir/Gider): ")
            description = input("Açıklama: ")
            amount = input("Tutar: ")
            add_transaction(date, category, description, amount)
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")

if __name__ == "__main__":
    main()
