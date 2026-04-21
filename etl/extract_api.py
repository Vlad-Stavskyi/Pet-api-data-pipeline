import requests

API_URL = "https://api.coingecko.com/api/v3/simple/price"

def fetch_crypto_prices():
    params = {
        "ids": "bitcoin,ethereum,solana",
        "vs_currencies": "usd",
        "include_market_cap": "true",
        "include_24hr_vol": "true",
        "include_24hr_change": "true",
        "include_last_updated_at": "true",
    }

    response = requests.get(API_URL, params=params, timeout=10)

    if response.status_code != 200:
        raise Exception(f"API request failed with status code: {response.status_code}")

    data = response.json()

    print("Raw API response:")
    print(data)

    return data

def main():
    fetch_crypto_prices()

if __name__ == "__main__":
    main()