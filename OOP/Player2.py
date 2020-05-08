class Player:
    teamName = "Fenerbahçe"
    def __init__(self,name1):
        super().__init__()
        self.__name = name1 #? creating instance variable and __name is private member of the function

    
    @classmethod
    def showMessage(cls):
        return "Message from class method"
    
    @classmethod
    def getTeamName(cls):
        return cls.teamName
    
    @staticmethod
    def staticMethod(times):
        print("Static Method "* times) 

    @staticmethod
    def __privateStaticMethod():
        pass

Ferdi = Player("Ferdi")
print(Ferdi.showMessage())
print(Player.showMessage())
print(Player.getTeamName())
Ferdi.staticMethod(2)
print("________________")
Player.staticMethod(4)

# * Access the private member 
print(Ferdi._Player__name)