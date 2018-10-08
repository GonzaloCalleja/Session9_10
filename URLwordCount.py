
from urllib.request import urlopen
# line.decode() # to convert from byte to string

fpl = urlopen("http://paparoti.co.nf/rocket_simulator.html")

word = "rocket"
counter = 0

for line in fpl:
    line = line.decode()
    pos = 0
    while True:
        pos = line.find(word, pos)
        if pos != -1:
            counter += 1
            pos += 1
        else:
            break

print(counter)