import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5433,
    database="crypto_db",
    user="user",
    password="password"
)

cur = conn.cursor()

cur.execute("SELECT * FROM crypto_prices;")
rows = cur.fetchall()
for row in rows:
    print(row)

print("\nTop crypto by price:")
cur.execute("""
SELECT symbol, price_usd
FROM crypto_prices
ORDER BY price_usd DESC;
""")
for row in cur.fetchall():
    print(row)

print("\nCrypto with price > 1000:")
cur.execute("""
SELECT symbol, price_usd
FROM crypto_prices
WHERE price_usd > 1000;
""")
for row in cur.fetchall():
    print(row)

print("\nAverage price:")
cur.execute("""
SELECT AVG(price_usd)
FROM crypto_prices;
""")
print(cur.fetchone())

print("\nTotal market cap:")
cur.execute("""
SELECT SUM(market_cap)
FROM crypto_prices;
""")
print(cur.fetchone())

print("\nTop crypto by market cap:")
cur.execute("""
SELECT symbol, market_cap
FROM crypto_prices
ORDER BY market_cap DESC
LIMIT 1;
""")
print(cur.fetchone())

cur.close()
conn.close()