import pandas as pd

lendeborg = pd.read_csv("data/raw/lendeborg_stats.csv")
johnson = pd.read_csv("data/raw/johnson_stats.csv")

print("Lendeborg 2025-2026")
print(lendeborg.head())
print(lendeborg.shape)
print(lendeborg.dtypes)

print("\n Johnson Jr. 2025-2026")
print(johnson.head())
print(johnson.shape)
print(johnson.dtypes)
