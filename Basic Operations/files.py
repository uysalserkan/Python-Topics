file = open("simple.txt","r")

# ('r')-> okuma ('w' 'a' 'x') ->Yazma  ('r+' 'w+' 'a+' 'x+')-> okuma ve yazma
# file.write("Something.")
reading = file.read()
print(reading)
file.close()