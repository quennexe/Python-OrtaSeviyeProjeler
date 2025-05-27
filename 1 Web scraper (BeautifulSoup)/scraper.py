import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Hata varsa tetikler
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Örnek: Sayfadaki tüm başlıkları (h1) çekelim
        titles = soup.find_all('h1')
        if not titles:
            print("Sayfada h1 etiketi bulunamadı.")
        else:
            print(f"Sayfadaki {len(titles)} tane <h1> etiketi:")
            for idx, title in enumerate(titles, 1):
                print(f"{idx}. {title.get_text(strip=True)}")

    except requests.exceptions.RequestException as e:
        print(f"Web sitesine erişirken hata oluştu: {e}")

def main():
    print("🌐 Basit Web Kazıyıcı (Web Scraper)")
    url = input("Kazımak istediğiniz web sitesinin URL'sini girin: ")
    scrape_website(url)

if __name__ == "__main__":
    main()
