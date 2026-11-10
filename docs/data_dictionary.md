# Data Dictionary

## Dataset Overview

This dataset contains game-by-game statistics for Yaxel Lendeborg and Morez Johnson Jr. during the 2025–2026 NCAA men's basketball season.

Each row represents one player's performance in one game.

## Column Definitions

| Column | Description | Data Type |
|---|---|---|
| Rk | Ranking or row index in the original source | Integer |
| Gcar | Career game number | Integer |
| Gtm | Team game number | Integer |
| Date | Date of the game | Date |
| Team | Player's team | String |
| Opp | Opposing team | String |
| Type | Game type or competition designation | String |
| Result | Game outcome and score | String |
| GS | Whether the player started the game | Boolean / Integer |
| MP | Minutes played | Numeric |
| FG | Field goals made | Integer |
| FGA | Field goals attempted | Integer |
| FG% | Field-goal percentage | Numeric |
| 3P | Three-pointers made | Integer |
| 3PA | Three-pointers attempted | Integer |
| 3P% | Three-point percentage | Numeric |
| 2P | Two-pointers made | Integer |
| 2PA | Two-pointers attempted | Integer |
| 2P% | Two-point percentage | Numeric |
| eFG% | Effective field-goal percentage | Numeric |
| FT | Free throws made | Integer |
| FTA | Free throws attempted | Integer |
| FT% | Free-throw percentage | Numeric |
| ORB | Offensive rebounds | Integer |
| DRB | Defensive rebounds | Integer |
| TRB | Total rebounds | Integer |
| AST | Assists | Integer |
| STL | Steals | Integer |
| BLK | Blocks | Integer |
| TOV | Turnovers | Integer |
| PF | Personal fouls | Integer |
| PTS | Total points scored | Integer |
| GmSc | Game Score, a summary measure of individual game performance | Numeric |

## Notes and Considerations

- Each row represents one player-game observation.
- The dataset contains two players from the 2025–2026 Michigan men's basketball season.
- Percentages should be checked to determine whether they are represented as decimals or whole percentages.
- The original raw datasets should remain unchanged.
- The blank column in the original source should be investigated before removal.
- Column definitions and source-specific abbreviations should be verified against the original data provider.
