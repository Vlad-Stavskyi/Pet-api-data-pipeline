import pandas as pd


def transform_crypto_data(data):
    records = []

    for coin, values in data.items():
        record = {
            "symbol": coin,
            "price_usd": values.get("usd"),
            "market_cap": values.get("usd_market_cap"),
            "volume_24h": values.get("usd_24h_vol"),
            "change_24h": values.get("usd_24h_change"),
            "last_updated": values.get("last_updated_at"),
        }

        records.append(record)

    df = pd.DataFrame(records)

    print("\nTransformed DataFrame:")
    print(df)

    return df