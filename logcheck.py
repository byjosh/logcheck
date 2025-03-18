from datetime import datetime
from sys import argv

minutes = set(range(0,60))

# dictionary to record hours seen in file
present ={3:{ n:{} for n in range(16,32)},4:{ n:{} for n in range(1,31)}}

#prepopulate with months, days , hours
for m in present:
    for d in present[m]:
        present[m][d] = { n:{} for n in range(0,24)}
        for h in present[m][d]:
            present[m][d][h] = set()

# print(present)

def get_datetime(line):
    if line.find("]") != -1:
        firstfield = line.split("]")[0]
        date_and_time = firstfield.strip("[")
        this_date = datetime.fromisoformat(date_and_time)
        return this_date
    elif line.find("]") == -1:
        return None

from os import path
# check log file/copy exists
if len(argv) > 1 and path.isfile(argv[1]):
    with open(argv[1]) as file:
        for line in file:
            this_day = get_datetime(line)
            if this_day is not None:
                # add the minutes seen to present dictionary
                present[this_day.month][this_day.day][this_day.hour].add(this_day.minute)
        now = datetime.now()
        for m in present:
            for d in present[m]:
                if (m < (now.month + 1)) and (d < (now.day + 1)):
                    for h in present[m][d]:
                        if len(present[m][d][h]) == 0:
                            print(f'{m}-{d} {h}hr not seen at all')
                        if len(present[m][d][h]) != 0 and len(present[m][d][h]) < len(minutes):
                            # if all minutes in hour represented then do not worry - only show found & missing minutes if minutes are missing
                            missing_minutes = minutes.difference(present[m][d][h])
                            found_minutes = minutes.intersection(present[m][d][h])
                            print(f'for {m}-{d} {h}hr :{len(missing_minutes)} minutes not seen in log - \n seen: {found_minutes}\n NOT seen: {missing_minutes}')
    
    
