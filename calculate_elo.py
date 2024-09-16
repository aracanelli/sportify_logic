class Games:
    def __init__(self):
        self.elo_const = 0.3
        self.k_const = 100

        self.team1 = []
        self.team1_elo = 0

        self.team2 = []
        self.team2_elo = 0

        self.E1 = 0.0
        self.E2 = 0.0
        self.E3 = 0.0
        self.E4 = 0.0

        self.winner_team_index = 0

    def set_team(self, player1, player2, player3, player4, score1, score2):
        self.team1 = [player1, player2]
        self.team1_elo = (player1.elo + player2.elo) / 2
        self.team2 = [player3, player4]
        self.team2_elo = (player3.elo + player4.elo) / 2

        # Compute the expected result
        self.compute_expected_result()
        self.set_winner(score1, score2)
        self.update_plusminus(player1, player2, player3, player4, score1, score2)

    def compute_expected_result(self):
        self.E1 = 1.0 / (1.0 + pow(10.0, ((self.team1[0].elo - self.team2_elo) / (self.team1[0].elo * self.elo_const))))
        self.E2 = 1.0 / (1.0 + pow(10.0, ((self.team1[1].elo - self.team2_elo) / (self.team1[1].elo * self.elo_const))))
        self.E3 = 1.0 / (1.0 + pow(10.0, ((self.team2[0].elo - self.team1_elo) / (self.team2[0].elo * self.elo_const))))
        self.E4 = 1.0 / (1.0 + pow(10.0, ((self.team2[1].elo - self.team1_elo) / (self.team2[1].elo * self.elo_const))))

    def set_winner(self, score1, score2):
        if score1 > score2:

            self.winner_team_index = 1 
        elif score1 < score2:
            self.winner_team_index = 2
        else: self.winner_team_index = 0
        self.k_const = 10 * abs(score1 - score2)

    def update_plusminus(self, player1, player2, player3, player4, score1, score2):
        player1.plusminus += score1 - score2
        player2.plusminus += score1 - score2
        player3.plusminus += score2 - score1
        player4.plusminus += score2 - score1


    def update_elo(self):
        if self.winner_team_index == 1:
            # you can even make your k_const stronger for the difference in points, you'd update your input to accept score difference
            self.team1[0].elo = self.team1[0].elo + self.k_const * (self.E1)
            self.team1[1].elo = self.team1[1].elo + self.k_const * (self.E2)
            self.team2[0].elo = self.team2[0].elo + self.k_const * (-1 + self.E3)
            self.team2[1].elo = self.team2[1].elo + self.k_const * (-1 + self.E4)

            self.team1[0].wins = self.team1[0].wins + 1
            self.team1[1].wins = self.team1[1].wins + 1
            self.team2[0].losses = self.team2[0].losses + 1
            self.team2[1].losses = self.team2[1].losses + 1

            self.team1[0].wins_with[self.team1[1].id] += 1
            self.team1[1].wins_with[self.team1[0].id] += 1
            self.team2[0].losses_with[self.team2[1].id] += 1
            self.team2[1].losses_with[self.team2[0].id] += 1

        elif self.winner_team_index == 2:
            self.team1[0].elo = self.team1[0].elo + self.k_const * (-1 + self.E1)
            self.team1[1].elo = self.team1[1].elo + self.k_const * (-1 + self.E2)
            self.team2[0].elo = self.team2[0].elo + self.k_const * (self.E3)
            self.team2[1].elo = self.team2[1].elo + self.k_const * (self.E4)

            self.team1[0].losses = self.team1[0].losses + 1
            self.team1[1].losses = self.team1[1].losses + 1
            self.team2[0].wins = self.team2[0].wins + 1
            self.team2[1].wins = self.team2[1].wins + 1

            self.team1[0].losses_with[self.team1[1].id] += 1
            self.team1[1].losses_with[self.team1[0].id] += 1
            self.team2[0].wins_with[self.team2[1].id] += 1
            self.team2[1].wins_with[self.team2[0].id] += 1
        else:
            self.team1[0].ties = self.team1[0].ties + 1
            self.team1[1].ties = self.team1[1].ties + 1
            self.team2[0].ties = self.team2[0].ties + 1
            self.team2[1].ties = self.team2[1].ties + 1
            
            self.team1[0].ties_with[self.team1[1].id] += 1
            self.team1[1].ties_with[self.team1[0].id] += 1
            self.team2[0].ties_with[self.team2[1].id] += 1
            self.team2[1].ties_with[self.team2[0].id] += 1

class Player:
    def __init__(self, id, name, sub=False):
        self.id = id
        self.name = name
        self.elo = 1000
        self.sub = sub
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.plusminus = 0

        #elo_split_opponents = [[0] * max_id for _ in range(max_id)]
        self.wins_with = [0 for _ in range(100)]
        self.losses_with = [0 for _ in range(100)]
        self.ties_with = [0 for _ in range(100)]

    def get_win_rate(self):
        if self.wins + self.losses != 0:
            win_rate = round((self.wins/(self.wins + self.losses + self.ties))*100,1)
            return str(win_rate) + "%"
        else: return str(0) + "%"

    def average_plusminus(self):
        if self.wins + self.losses != 0:
            return round((self.plusminus)/((self.wins + self.losses + self.ties)/5), 2)
        else: return 0

    def get_win_rate_with(self, id):
        if self.wins_with[id] + self.losses_with[id] != 0:
            return round((self.wins_with[id]/(self.wins_with[id] + self.losses_with[id] + self.ties_with[i])) * 100, 2)
        else: return 0

class Team:
    def __init__(self, player1, player2, name):
        self.player1 = player1
        self.player2 = player2
        self.name = name