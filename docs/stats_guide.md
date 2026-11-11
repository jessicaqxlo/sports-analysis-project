# Summary Table
1. Season totals

The whole season added up (PTS, TRB, AST, MP, and so on). Larger for players with more minutes.

2. Minutes per game (MPG)

total minutes / games played. A role stat: how much the player is on the floor.

3. Per-40 stats (PTS_per40, TRB_per40, AST_per40, STL_BLK_per40, TOV_per40)

What a player produces per 40 minutes on the floor.

stat_per40 = total stat / total minutes * 40

Similar in spirit to "per game," but standardized to 40 minutes instead of however many minutes the player happened to play. This keeps a starter and a bench player comparable.
Per-40 numbers are higher than per-game numbers for players who play under 40 minutes a game.
TOV_per40 is turnovers per 40 minutes. It is not turnover percentage, which is a different stat.
4. Rates and percentages (no time involved)
Stat	Formula	Plain meaning
eFG_pct	(FG + 0.5 * 3P) / FGA	Shooting efficiency on field goal attempts, giving threes extra credit
TS_pct	PTS / (2 * (FGA + 0.44 * FTA))	Scoring efficiency counting free throws too
3PA_rate	3PA / FGA	Share of a player's shots that are threes

The gap between TS_pct and eFG_pct shows how much free throws help a player's efficiency.