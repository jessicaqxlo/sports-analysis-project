import pandas as pd

# process lendeborg data
lendeborg = pd.read_csv("data/raw/lendeborg_stats.csv")
lendeborg = lendeborg.drop(lendeborg.index[-1])
lendeborg = lendeborg.rename(columns={"Unnamed: 5": "Venue"}, inplace=True)

# process johnson data
johnson = pd.read_csv("data/raw/johnson_stats.csv")
johnson = johnson.drop(johnson.index[-1])
johnson = johnson.rename(columns={"Unnamed: 5": "Venue"}, inplace=True)


print("Lendeborg 2025-2026")
print(lendeborg.head())
print("\n Johnson Jr. 2025-2026")
print(johnson.head())

