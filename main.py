import sys
from model.file import File
from model.output import Rich
from controller.timesheet import TimeSheet


filename = sys.argv[1]
lines = File().read(filename)
minutes = 0
for line in lines:
    print (TimeSheet().analyse_line(line))
    minutes += TimeSheet().analyse_line(line)
    

Rich().time_print(minutes)
