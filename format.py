string1="Ser"
string2="kan"
string3="öz"

print("{}{} {}{}".format(string1,string2,string3,string2))
print("{1}{0} {3}{2}".format(string2,string1,string2,string3))
print("|{:>15}|{:<15}| {ad}{soyad}".format(string1,string2,ad = string3,soyad=string2))
print("|{:^15}|{:s} {}{}".format(string1,string2,string3,string2))