class Player:
    teamName = "Fenerbahce" #? class variable
    # formerTeams=[] 
    teamMembers = []
    #? above is wrong because all objects share this variable.
    def __init__(self,name):
        super().__init__()
        self.name = name #? creating instance variable
        self.teamMembers.append(name) 
        self.formerTeams=[] #? True for our purpose




    def displayInfo(self):
        print("Name: "+ self.name + " Teamname: "+ self.teamName + "Former Teams: ")
        print(self.formerTeams)

P1 = Player("Ferdi")
P1.formerTeams.append("unknown")
P2 = Player("Altay")
P2.formerTeams.append("altay")
P1.displayInfo()
P2.displayInfo()
print(Player.teamMembers)