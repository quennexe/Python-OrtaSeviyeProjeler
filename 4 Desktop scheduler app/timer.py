import tkinter as tk
from tkinter import messagebox

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Masaüstü Zamanlayıcı / Desktop Timer")

        self.time_var = tk.StringVar()
        self.time_var.set("00:00:00")

        self.label = tk.Label(root, textvariable=self.time_var, font=("Helvetica", 48))
        self.label.pack(pady=20)

        self.entry = tk.Entry(root, width=8, font=("Helvetica", 24))
        self.entry.insert(0, "00:01:00")  # Varsayılan 1 dakika
        self.entry.pack()

        self.start_button = tk.Button(root, text="Başlat / Start", command=self.start_timer)
        self.start_button.pack(pady=5)

        self.reset_button = tk.Button(root, text="Sıfırla / Reset", command=self.reset_timer)
        self.reset_button.pack()

        self.remaining_seconds = 0
        self.timer_running = False

    def start_timer(self):
        if not self.timer_running:
            time_str = self.entry.get()
            try:
                h, m, s = map(int, time_str.split(":"))
                self.remaining_seconds = h * 3600 + m * 60 + s
                if self.remaining_seconds <= 0:
                    raise ValueError
                self.count_down()
                self.timer_running = True
            except:
                messagebox.showerror("Hata / Error", "Lütfen geçerli bir süre girin (HH:MM:SS)")

    def count_down(self):
        if self.remaining_seconds > 0:
            h = self.remaining_seconds // 3600
            m = (self.remaining_seconds % 3600) // 60
            s = self.remaining_seconds % 60
            self.time_var.set(f"{h:02d}:{m:02d}:{s:02d}")
            self.remaining_seconds -= 1
            self.root.after(1000, self.count_down)
        else:
            self.time_var.set("00:00:00")
            messagebox.showinfo("Bitti! / Time's up!", "Zamanlayıcı sona erdi.")
            self.timer_running = False

    def reset_timer(self):
        self.timer_running = False
        self.time_var.set("00:00:00")

def main():
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
