from model.time import Time
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
    

Rich().time_print(f"{minutes} minutes")
hours, left_minutes = Time().convert_minutes_to_hours_and_minutes(minutes)
Rich().time_print(f"{hours} hours and {left_minutes} minutes")