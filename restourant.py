desks = dict()
for i in range(10):
   desks[i]=0


def addRecepies():
   deskNo=int(input("Desk No: "))
   deskNo-=1
   current=desks[deskNo]
   getting_meals=float(input("How many fee: "))
   recepies=current+getting_meals
   desks[deskNo]=recepies

def removeRecepies():
   deskNo=int(input("Desk No: "))
   deskNo-=1
   current=desks[deskNo]
   remove_fee=float(input("How many fee: "))
   recepies=float(current)-remove_fee
   if recepies<0:
      print("Please check your removing fee!")
   else:
      desks[deskNo]=recepies

def checkRecepies(file):
   try:
      raw=open(file)
      recepies=raw.read()
      recepies=recepies.split("\n")
      recepies.pop()
      raw.close()
      recepies_not_created=True

   except FileNotFoundError:
      raw=open(file,"w")
      raw.close()
      print("Your raw recepies was be deleted, find your administration..")
      print("File created again..")
      recepies_not_created=False
   if recepies_not_created:
      for i in enumerate(recepies):
         desks[i[0]]=float(i[1])
   else:
      pass


def updateRecepies(file):
   raw=open(file,"w")
   for i in range(10):
      fee=desks[i]
      fee=str(fee)
      raw.write(fee + "\n")
   raw.close()

def main():
   checkRecepies("recepies.txt")
   while True:
      print("""
      [1] Show Desks
      [2] Get Recepies
      [3] Delete Desk
      [Q] Exit Program
      """)
      
      usr_input=input("Please enter your option: ")

      if usr_input == "1":
         for i in range(10):
            print("${} for the desk\t->\t {}".format(desks[i],i))
         print("Please enter for back to the menu")
         input()

      elif usr_input=="2":
         addRecepies()
         print("Please enter for back to the menu")
         input()
      elif usr_input=="3":
         removeRecepies()
         print("Please enter for back to the menu")
         input()

      elif usr_input=="Q" or usr_input=="q":
         updateRecepies("recepies.txt")
         print("Program was be terminated in the memory...")
         exit()

main()