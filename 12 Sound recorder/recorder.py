import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(duration, filename="recorded.wav", samplerate=44100):
    print(f"{duration} saniye boyunca ses kaydediliyor...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2)
    sd.wait()
    write(filename, samplerate, recording)
    print(f"Ses kaydı tamamlandı: {filename}")

def main():
    print("🎙️ Ses Kaydedici Uygulaması")
    try:
        duration = float(input("Kayıt süresi (saniye): "))
        filename = input("Kaydedilecek dosya ismi (örn: ses.wav): ").strip() or "recorded.wav"
        record_audio(duration, filename)
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    main()
