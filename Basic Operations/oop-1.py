class User():
    def __init__(self,inname:str):
        self.name=inname
        self.somelist=[]
    def Yazdir(self):
        print(self.name , "\n", self.somelist)

class Admin(User):
    def __init__(self,inname:str,insurname:str,position:str):
        self.inname=inname
        self.insurname=insurname
        self.position=position

    def adminYaz(self):
        print(self.inname,self.insurname,self.position)
        print("Admin bey")

class Moderator(User):
    def __init__(self,inname:str,insurname:str):
        super().__init__(inname)
        self.insurname=insurname

someone = User("Ahmetovaic")
someone.somelist += ["Falan"]
someone.somelist += ["Filan"]
print(someone.name)
print(someone.somelist)
print()
someone.Yazdir()

Boys=Moderator("Boyas","Anılar")
Boys.Yazdir()

Adebayor=Admin("Adnan","Yok","özel abiriyim")
Adebayor.adminYaz()

if __name__ == "__main__":
    print("ana dosya")
else:
    print("başka dosyadan çağırıldı, ana dosya import edildi")

