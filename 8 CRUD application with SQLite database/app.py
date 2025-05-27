import sqlite3

DB_NAME = "contacts.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_contact(name, phone):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', (name, phone))
    conn.commit()
    conn.close()
    print(f"{name} başarıyla eklendi.")

def list_contacts():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contacts')
    rows = cursor.fetchall()
    conn.close()
    if rows:
        print("Kişiler Listesi:")
        for row in rows:
            print(f"ID: {row[0]}, İsim: {row[1]}, Telefon: {row[2]}")
    else:
        print("Kayıtlı kişi bulunmamaktadır.")

def update_contact(contact_id, new_name, new_phone):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('UPDATE contacts SET name = ?, phone = ? WHERE id = ?', (new_name, new_phone, contact_id))
    conn.commit()
    conn.close()
    print(f"ID {contact_id} başarıyla güncellendi.")

def delete_contact(contact_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))
    conn.commit()
    conn.close()
    print(f"ID {contact_id} başarıyla silindi.")

def main():
    create_table()

    while True:
        print("\nSQLite CRUD Uygulaması")
        print("1. Kişi Ekle")
        print("2. Kişileri Listele")
        print("3. Kişi Güncelle")
        print("4. Kişi Sil")
        print("5. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            name = input("İsim: ")
            phone = input("Telefon: ")
            add_contact(name, phone)
        elif choice == "2":
            list_contacts()
        elif choice == "3":
            contact_id = input("Güncellenecek ID: ")
            new_name = input("Yeni İsim: ")
            new_phone = input("Yeni Telefon: ")
            update_contact(contact_id, new_name, new_phone)
        elif choice == "4":
            contact_id = input("Silinecek ID: ")
            delete_contact(contact_id)
        elif choice == "5":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
