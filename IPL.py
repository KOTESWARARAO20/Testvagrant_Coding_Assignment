class IPL:
    total_results = []
    @staticmethod
    def table(team_result):
        IPL.total_results.append(team_result)
    @staticmethod
    def team_with_2_consecutive_losses():
        print('========== TEAMS WITH 2 CONSECUTIVE LOSSES ==========')
        team_count = 0
        points = 0
        for i in IPL.total_results:
            for j in range(1, len(i[2])):
                if i[2][j] == False and i[2][j - 1] == False:
                    team_count += 1
                    points += i[1]
                    print(i[0])
                    break
        print(f"Teams with 2 consecutive losses: {team_count}")
        print(f"Average points of teams with 2 consecutive losses: {round(points / team_count, 2)}")
    @staticmethod
    def team_with_2_consecutive_wins():
        print('========== TEAMS WITH 2 CONSECUTIVE WINS ==========')
        team_count = 0
        points = 0
        for i in IPL.total_results:
            for j in range(1, len(i[2])):
                if i[2][j] == True and i[2][j - 1] == True:
                    team_count += 1
                    points += i[1]
                    print(i[0])
                    break
        print(f"Teams with 2 consecutive losses: {team_count}")
        print(f"Average points of teams with 2 consecutive losses: {round(points / team_count, 2)}")
class Team(IPL):
    def init(self, name, points, results):self.name = name
        self.points = points
        self.results = results
        IPL.table([self.name, self.points, self.results])
team1 = Team("GT", 20, [True, True, False, False, True])
team2 = Team("LSG", 18, [True, False, False, True, True])
team3 = Team("RR", 16, [True, False, True, False, False])
team4 = Team("DC", 14, [True, True, False, True, False])
team5 = Team("RCB", 14, [False, True, True, False, False])
team6 = Team("KKR", 12, [False, True, True, False, True])
team7 = Team("PBKS", 12, [False, True, False, True, False])
team8 = Team("SRH", 12, [True, False, False, False, False])
team9 = Team("CSK", 8, [False, False, True, False, True])
team10 = Team("MI", 6, [False, True, False, True, True])
ipl = IPL()
ipl.team_with_2_consecutive_losses()
ipl.team_with_2_consecutive_wins()

