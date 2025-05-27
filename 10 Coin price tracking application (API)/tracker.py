import requests

def get_coin_price(coin_id="bitcoin", currency="usd"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        price = data[coin_id][currency]
        print(f"{coin_id.capitalize()} fiyatı ({currency.upper()}): {price}")
    except requests.exceptions.RequestException as e:
        print(f"API isteği başarısız oldu: {e}")

def main():
    print("Coin Fiyat Takip Uygulaması / Coin Price Tracker")
    coin_id = input("Takip etmek istediğiniz coin ID'si (örn: bitcoin, ethereum): ").lower()
    currency = input("Fiyatın hangi para birimi ile gösterilmesini istiyorsunuz? (örn: usd, eur): ").lower()

    get_coin_price(coin_id, currency)

if __name__ == "__main__":
    main()
