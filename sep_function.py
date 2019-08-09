print("T", "B", "M", "M", sep = ".", end = " Say Hello\n")
adiniz = input("Adinizi giriniz: ")
print("Adiniz: ", adiniz)
print("girdiler her zaman string olarak gelir.")

num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
print("Your score is: ", num1+num2)
if (num1 == 5 or num2 == 5):
    print(num1 + " veya " + num2 + " 5'e eşit.")
elif (num1 == 5 and num2 == 5):
    print(num1 + " ve " + num2 + " 5'e eşit.")
if not (adiniz):
    print("Adinizin memory değeri null değildir.")
if ("kan" in adiniz):
    print("adinizin içinde kan var.")
