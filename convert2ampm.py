import os
from datetime import datetime
import pprint
os.chdir('/Users/Ryan De Villas/documents/Python')
def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v
 

pprint.pprint(flights)
print()

fts = {convert2ampm(k): v.title() for k,v in flights.items()}
print('\n')
pprint.pprint(fts)

# fts3 = {}
# for k, v in fts.items():
#     for dest in set(fts.values()):
#             if v == dest:
#                 fts3[dest] = k


print('\n')
print(fts.items())
    
        

print('\n')
pprint.pprint(fts3)

fts4 = {dest: [k for k, v in fts.items() if v == dest] for dest in set(fts.values())}
print('\n')
pprint.pprint(fts4)

# fts3 = {for k, v in flights.items()}

##dest = set(fts.values())
##print(dest)

##fts2 = {}
##for dest in set(fts.values()):
##    fts2[dest] = {k for k, v in fts.items() if v == dest}
##print('\n')
##pprint.pprint(fts2)

# fts2 = {dest : [k for  k, v in fts.items() if v == dest] for dest in set(fts.values()) }
# print('\n')
# pprint.pprint(fts2)




        
