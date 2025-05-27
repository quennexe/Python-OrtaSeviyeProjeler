import tkinter as tk
from tkinter import messagebox
import json
import random
import string
import os

DATA_FILE = "data.json"

class PasswordManager:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI Parola Yöneticisi / GUI Password Manager")

        # Site Adı
        tk.Label(root, text="Site Adı / Website:").grid(row=0, column=0, pady=5, sticky="e")
        self.website_entry = tk.Entry(root, width=35)
        self.website_entry.grid(row=0, column=1, pady=5, sticky="w")

        # Kullanıcı Adı / Email
        tk.Label(root, text="Kullanıcı Adı / Email:").grid(row=1, column=0, pady=5, sticky="e")
        self.username_entry = tk.Entry(root, width=35)
        self.username_entry.grid(row=1, column=1, pady=5, sticky="w")

        # Parola
        tk.Label(root, text="Parola / Password:").grid(row=2, column=0, pady=5, sticky="e")
        self.password_entry = tk.Entry(root, width=21)
        self.password_entry.grid(row=2, column=1, pady=5, sticky="w")

        # Parola Üret Butonu
        self.generate_button = tk.Button(root, text="Parola Üret / Generate Password", command=self.generate_password)
        self.generate_button.grid(row=2, column=2, padx=5)

        # Kaydet Butonu
        self.save_button = tk.Button(root, text="Kaydet / Save", width=36, command=self.save_password)
        self.save_button.grid(row=3, column=1, columnspan=2, pady=10)

        # Arama Butonu
        self.search_button = tk.Button(root, text="Ara / Search", width=13, command=self.search_password)
        self.search_button.grid(row=0, column=2, padx=5)

    def generate_password(self):
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(12))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    def save_password(self):
        website = self.website_entry.get().strip()
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not website or not username or not password:
            messagebox.showwarning("Uyarı / Warning", "Lütfen tüm alanları doldurun.")
            return

        new_data = {
            website: {
                "username": username,
                "password": password
            }
        }

        try:
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, "r") as file:
                    data = json.load(file)
            else:
                data = {}

            data.update(new_data)

            with open(DATA_FILE, "w") as file:
                json.dump(data, file, indent=4)

            messagebox.showinfo("Başarılı / Success", f"{website} için bilgiler kaydedildi.")
            self.website_entry.delete(0, tk.END)
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Hata / Error", f"Dosya işlemi sırasında hata oluştu: {e}")

    def search_password(self):
        website = self.website_entry.get().strip()
        if not website:
            messagebox.showwarning("Uyarı / Warning", "Lütfen aramak için site adını girin.")
            return

        try:
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, "r") as file:
                    data = json.load(file)
                if website in data:
                    username = data[website]["username"]
                    password = data[website]["password"]
                    messagebox.showinfo(f"{website} Bilgileri", f"Kullanıcı Adı: {username}\nParola: {password}")
                else:
                    messagebox.showinfo("Bulunamadı / Not Found", f"{website} için kayıt bulunamadı.")
            else:
                messagebox.showinfo("Dosya Yok", "Henüz kayıtlı bir veri dosyası yok.")
        except Exception as e:
            messagebox.showerror("Hata / Error", f"Dosya okunurken hata oluştu: {e}")

def main():
    root = tk.Tk()
    app = PasswordManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()
