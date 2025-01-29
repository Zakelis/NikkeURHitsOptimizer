import Utilities
from Boss import Boss
from Player import Player
from Hit import Hit


class Summary:
    def __init__(self):
        self.players = []  # List of players that mocked
        self.bossesHits = []  # [Boss][Hit] 2-dimension array, all hits per boss

        self.B1T1 = None
        self.B2T1 = None
        self.B3T1 = None
        self.B4T1 = None
        self.B5T1 = None
        self.B1T2 = None
        self.B2T2 = None
        self.B3T2 = None
        self.B4T2 = None
        self.B5T2 = None
        self.bosses = []

        self.hp_list_ref = [
            ("Laitance", 29225662800),
            ("Heavy Metal", 29225662800),
            ("Nihilister", 65385671800),
            ("Rb Obelisk", 29225662800),
            ("Gravedigger", 47553215600),
            ("Laitance", 137302384800),
            ("Heavy Metal", 137302384800),
            ("Nihilister", 207407492800),
            ("Rb Obelisk", 137302384800),
            ("Gravedigger", 140841813600)
        ]

    def feedPlayersArray(self, parsedHits):
        exploredPlayers = []
        for hit in parsedHits:
            playerName = Utilities.getFirstListItem(hit)
            if playerName not in exploredPlayers:
                exploredPlayers.append(playerName)
                player = Player(playerName)
                self.players.append(player)

    def feedBossesList(self):
        self.B1T1 = Boss("Laitance", 29225662800)
        self.bosses.append(self.B1T1)
        self.B2T1 = Boss("Heavy Metal", 29225662800)
        self.bosses.append(self.B2T1)
        self.B3T1 = Boss("Nihilister", 65385671800)
        self.bosses.append(self.B3T1)
        self.B4T1 = Boss("Rb Obelisk", 29225662800)
        self.bosses.append(self.B4T1)
        self.B5T1 = Boss("Gravedigger", 47553215600)
        self.bosses.append(self.B5T1)
        self.B1T2 = Boss("Laitance", 137302384800)
        self.bosses.append(self.B1T2)
        self.B2T2 = Boss("Heavy Metal", 137302384800)
        self.bosses.append(self.B2T2)
        self.B3T2 = Boss("Nihilister", 207407492800)
        self.bosses.append(self.B3T2)
        self.B4T2 = Boss("Rb Obelisk", 137302384800)
        self.bosses.append(self.B4T2)
        self.B5T2 = Boss("Gravedigger", 140841813600)
        self.bosses.append(self.B5T2)
        print("After feeding bosses list")
        for boss in self.bosses:
            print(boss.name, boss.hp)

    def feedPlayerHits(self, parsedHits):
        print("feedPlayerHits START")
        self.feedPlayersArray(parsedHits)

        print(self.players.__len__(), "players have mocked so far :")
        for player in self.players:
            print(player.name)
