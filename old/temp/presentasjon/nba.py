'''
Descriptions for the columns:

    Rk : Rank
    Player : Player's name
    Pos : Position
    Age : Player's age
    Tm : Team
    G : Games played
    GS : Games started
    MP : Minutes played per game
    FG : Field goals per game
    FGA : Field goal attempts per game
    FG% : Field goal percentage
    3P : 3-point field goals per game
    3PA : 3-point field goal attempts per game
    3P% : 3-point field goal percentage
    2P : 2-point field goals per game
    2PA : 2-point field goal attempts per game
    2P% : 2-point field goal percentage
    eFG% : Effective field goal percentage
    FT : Free throws per game
    FTA : Free throw attempts per game
    FT% : Free throw percentage
    ORB : Offensive rebounds per game
    DRB : Defensive rebounds per game
    TRB : Total rebounds per game
    AST : Assists per game
    STL : Steals per game
    BLK : Blocks per game
    TOV : Turnovers per game
    PF : Personal fouls per game
    PTS : Points per game

'''
import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset
nba_data = pd.read_csv('nba.csv', index_col=0, sep=';', encoding='latin1')

# -	Hvordan finner du ut hvilken spiller som har spilt flest kamper?
#most_games = nba_data.loc[nba_data['G'].idxmax()]
# Alternativt:
most_games = nba_data.nlargest(1, 'G').iloc[0]
print(f"Player with most games played: {most_games['Player']} with {most_games['G']} games.")

# -	Hvordan kan du finne ut hvor mange spillere som spiller for laget "LAL"?
num_players_lal = nba_data[nba_data['Tm'] == 'LAL'].shape[0]
# Applying this mask to nba_data returns a new DataFrame containing only the Lakers players. 
# The .shape[0] part then retrieves the number of rows in this filtered DataFrame, which corresponds to the number of Lakers players. The result is stored in the variable num_players_lal.
print(f"\n\nNumber of players in team LAL: {num_players_lal}")
# Alternativt:
# num_players_lal = nba_data['Tm'].value_counts().get('LAL', 0)

# -	Hvordan kan du finne ut hvor mange forskjellige posisjoner ("Pos") som finnes i datasettet?
num_positions = nba_data['Pos'].nunique()
print(f"\n\nNumber of unique positions: {num_positions}")
# Hva er om du vil ha en liste over posisjonene?
unique_positions = nba_data['Pos'].unique()
print(f"Unique positions: {', '.join(unique_positions)}")

# -	Hvordan kan du finne gjennomsnittsalderen til alle spillerne?
average_age = nba_data['Age'].mean()
print(f"\n\nAverage age of players: {average_age:.2f} years")

# -	Hvordan kan du finne ut hvilken spiller som har høyest "PTS" (poeng per kamp)?
highest_pts_player = nba_data.nlargest(1, 'PTS').iloc[0]
print(f"\n\nPlayer with highest points per game: {highest_pts_player['Player']} with {highest_pts_player['PTS']} points.")

# -	Hvordan kan du finne ut hvilke spillere som har en "3P%" over 0.4?
high_3p_players = nba_data[nba_data['3P%'] > 0.4]
print("\n\nPlayers with 3-point percentage over 0.4:")
for index, row in high_3p_players.iterrows():
    print(f"{row['Player']} with 3P%: {row['3P%']}")

# -	Hvordan kan du regne ut totalen av "TRB" (total rebounds) for alle spillere på laget "BOS"?
total_trb_bos = nba_data[nba_data['Tm'] == 'BOS']['TRB'].sum()
print(f"\n\nTotal rebounds for team BOS: {total_trb_bos}")

# -	Hvordan kan du finne ut hvilke spillere som har spilt mer enn 30 minutter per kamp og har en "FG%" over 0.5?
high_fg_minutes_players = nba_data[(nba_data['MP'] > 30) & (nba_data['FG%'] > 0.5)]
print("\n\nPlayers with more than 30 minutes per game and FG% over 0.5:")
for index, row in high_fg_minutes_players.iterrows():
    print(f"{row['Player']} with FG%: {row['FG%']} and MP: {row['MP']}")

# -	Hvordan kan du finne ut hvilken spiller som har høyest "AST" (assists per kamp) på laget "DEN"?
highest_ast_den = nba_data[nba_data['Tm'] == 'DEN'].nlargest(1, 'AST').iloc[0]
print(f"\n\nPlayer with highest assists per game in team DEN: {highest_ast_den['Player']} with {highest_ast_den['AST']} assists.")

# - -	Hvordan kan du finne ut hvilke spillere som har både over 20 poeng per kamp og over 5 assists per kamp?
high_pts_ast_players = nba_data[(nba_data['PTS'] > 20) & (nba_data['AST'] > 5)]
print("\n\nPlayers with more than 20 points and more than 5 assists per game:")
for index, row in high_pts_ast_players.iterrows():
    print(f"{row['Player']} with PTS: {row['PTS']} and AST: {row['AST']}")

# -	Hvordan kan du finne ut hvilken posisjon ("Pos") som i gjennomsnitt scorer flest poeng per kamp?
average_pts_by_pos = nba_data.groupby('Pos')['PTS'].mean().sort_values(ascending=False)
print("\n\nAverage points per game by position:")
for pos, pts in average_pts_by_pos.items():
    print(f"{pos}: {pts:.2f} points")

# Tegn et stolpediagram for å visualisere forrige spørsmål
average_pts_by_pos.plot(kind='bar', color='skyblue')
plt.title('Average Points per Game by Position')
plt.xlabel('Position')
plt.ylabel('Average Points')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()