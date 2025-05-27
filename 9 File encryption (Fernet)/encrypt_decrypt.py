from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Anahtar oluşturuldu ve 'secret.key' dosyasına kaydedildi.")

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(file_path, key):
    f = Fernet(key)
    with open(file_path, "rb") as file:
        data = file.read()
    encrypted = f.encrypt(data)
    with open(file_path + ".encrypted", "wb") as file:
        file.write(encrypted)
    print(f"{file_path} dosyası şifrelendi.")

def decrypt_file(encrypted_path, key):
    f = Fernet(key)
    with open(encrypted_path, "rb") as file:
        encrypted_data = file.read()
    decrypted = f.decrypt(encrypted_data)
    original_path = encrypted_path.replace(".encrypted", ".decrypted")
    with open(original_path, "wb") as file:
        file.write(decrypted)
    print(f"{encrypted_path} dosyası çözüldü ve {original_path} olarak kaydedildi.")

def main():
    print("Dosya Şifreleme / Deşifreleme (Fernet)")

    while True:
        print("\nSeçenekler:")
        print("1. Anahtar Oluştur")
        print("2. Dosya Şifrele")
        print("3. Dosya Deşifrele")
        print("4. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            generate_key()
        elif choice == "2":
            path = input("Şifrelenecek dosya yolu: ")
            try:
                key = load_key()
                encrypt_file(path, key)
            except FileNotFoundError:
                print("Anahtar dosyası bulunamadı. Lütfen önce anahtar oluşturun.")
        elif choice == "3":
            path = input("Deşifrelenecek dosya yolu: ")
            try:
                key = load_key()
                decrypt_file(path, key)
            except FileNotFoundError:
                print("Anahtar dosyası bulunamadı. Lütfen önce anahtar oluşturun.")
            except Exception as e:
                print(f"Bir hata oluştu: {e}")
        elif choice == "4":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")

if __name__ == "__main__":
    main()
