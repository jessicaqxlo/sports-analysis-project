import pandas as pd

# Read data into a dataframe
player_data = pd.read_csv("data/processed/processed_data.csv")

stat_cols = ["MP", "PTS", "TRB", "AST", "STL", "BLK", "TOV", "FG", "FGA", "FTA", "3P", "3PA"]

# Construct season totals summary table
totals = player_data.groupby("Player")[stat_cols].sum()
totals["Games"] = player_data.groupby("Player").size()
# print(totals.head())

# Create table scaled to stats per minute played
per40_cols = ["PTS", "TRB", "AST", "STL", "BLK", "TOV"]

for col in per40_cols:
    totals[col + "_per40"] = totals[col] / totals["MP"] * 40

# Additional Stats
totals["STL_BLK_per40"] = (totals["STL"] + totals["BLK"]) / totals["MP"] * 40
totals["MPG"] = totals["MP"] / totals["Games"]
totals["TS_pct"] = totals["PTS"] / (2 * (totals["FGA"] + 0.44 * totals["FTA"]))
totals["3PA_rate"] = totals["3PA"] / totals["FGA"]
totals["eFG_pct"] = (totals["FG"] + 0.5 * totals["3P"]) / totals["FGA"]
print(totals.round(3))

# Create table with comparisions
cols_to_compare = ["Games", "MPG", "PTS_per40", "TRB_per40", "AST_per40",
                   "STL_BLK_per40", "TOV_per40", "eFG_pct", "TS_pct", "3PA_rate"]

compare = totals[cols_to_compare].round(3).T
p1, p2 = compare.columns
compare["Diff"] = (compare[p1] - compare[p2]).round(3)
print(compare)
