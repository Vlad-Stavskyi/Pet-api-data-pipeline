from sqlalchemy import create_engine

def load_to_postgres(df):
    engine = create_engine(
        "postgresql://user:password@localhost:5433/crypto_db"
    )

    df.to_sql(
        name="crypto_prices",
        con=engine,
        if_exists="replace",
        index=False
    )

    print("Data loaded to PostgreSQL!")