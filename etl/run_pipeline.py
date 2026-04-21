from extract_api import fetch_crypto_prices
from transform_data import transform_crypto_data
from load_data import load_to_postgres

def run_pipeline():
    data = fetch_crypto_prices()
    df = transform_crypto_data(data)
    load_to_postgres(df)

if __name__ == "__main__":
    run_pipeline()