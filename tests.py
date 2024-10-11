import itertools
import random

if __name__ == "__main__":
    players = [
        "Anthony",
        "Sarah",
        "Erica",
        "Miranda",
        "Anna",
        "Silvio",
        "Frank",
        "Justin"
    ]


# random.shuffle(players)
# Step 1: Generate unique pairs of players (teams)
teams = list(itertools.combinations(players, 2))

# Helper function to check if players have already been teammates
def no_repeat_teammates(combo, previous_teams):
    for team in combo:
        player1, player2 = team
        # If this pair of players has already been a team, return False
        if (player1, player2) in previous_teams or (player2, player1) in previous_teams:
            return False
    return True

# Step 2: Generate all combinations of 4 unique teams (2 courts, 4 teams in total)
valid_matchups = []
previous_teams = set()  # To track the teams that have been formed so far

for combo in itertools.combinations(teams, 4):  # Select 4 teams at a time
    # Get all players involved in the 4 selected teams
    all_players = set(itertools.chain.from_iterable(combo))
    # Ensure there are exactly 8 unique players (no overlap) and no repeating teammates
    if len(all_players) == 8 and no_repeat_teammates(combo, previous_teams):
        # Step 3: Split into 2 matchups for the 2 courts
        court1 = (combo[0], combo[1])  # First two teams on court 1
        court2 = (combo[2], combo[3])  # Next two teams on court 2
        valid_matchups.append((court1, court2))
        
        # Add the current teams to the set of previous teams
        previous_teams.update(combo)

# Step 4: Print all possible valid court matchups with no repeating teammates
i = 1  # Initialize the counter
print()
for (court1, court2) in valid_matchups:
    print(f"Game {i:02}: {court1[0][0].ljust(7)} + {court1[0][1].ljust(7)} vs {court1[1][0].ljust(7)} + {court1[1][1].ljust(7)} ")
    print(f"Game {i+1:02}: {court2[0][0].ljust(7)} + {court2[0][1].ljust(7)} vs {court2[1][0].ljust(7)} + {court2[1][1].ljust(7)}")
    i += 2
print()