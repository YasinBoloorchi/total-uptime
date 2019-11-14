from os import system
import re
system('last > ./last.txt')

lastFile = open('./last.txt', 'r')

uptimes = []

for l in lastFile.readlines():
    tempSuptime = re.findall('(\((.*\+)*(\d{2}:\d{2})\))', l)
    if len(tempSuptime) > 0:
        suptime = tempSuptime[0][2]
        uptimes.append(suptime)

minuteS = 0
hourS = 0

for t in uptimes:
    minute = int(t.split(':')[1])
    hour = int(t.split(':')[0])

    minuteS += minute
    hourS += hour

hourS += int(minuteS/60)
minuteS = minuteS % 60

lastFile.close()
system('rm ./last.txt')

print('uptime till now : {} hour and {} minutes'.format(hourS,minuteS))