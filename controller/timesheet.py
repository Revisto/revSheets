from os import confstr
import re
from model.file import File
from model.regex import Regex
from model.time import Time

class TimeSheet:
    def __init__(self):
        self.timesheet_patters = {
            "hour_to_hour": "^.*?(\d{1,2})[.:]*(\d{0,2})[^0-9:]+?(\d{1,2})[.:,]*(\d{0,2})",
            "hour_to_now": "^.*?(\d{1,2})[.:]*(\d{0,2})[^0-9:]+?NOW",
            "hour_and_minute": "^.*?(\d{1,2})[.:,]+(\d{0,2})",
            "minutes": "^[^0-9\n]*?(\d{1,})"
        }
    
    def customize_timesheet_patterns(self, pattern_name, sign):
        pattern = self.timesheet_patters[pattern_name]
        customized_pattern = pattern[0] + sign + pattern[1:]
        return customized_pattern

    def analyse_line(self, line):
        line = File().remove_extra_spaces(line)
        if line.startswith("+"):
            return + TimeSheet().analyse_time(line, "\+")
        if line.startswith("-"):
            return - TimeSheet().analyse_time(line, "-")
        return False


    def analyse_time(self, line, sign):
        hour_to_now_result = Regex().search(TimeSheet().customize_timesheet_patterns("hour_to_now", sign), line)
        if hour_to_now_result is not False:
            if hour_to_now_result[1] == "":
                hour_to_now_result[1] = 0
            time1 = int(hour_to_now_result[0])*60 + int(hour_to_now_result[1])
            time2 = Time().current_minutes()
            if time2 < time1:
                time2 += 12*60
            return time2 - time1
            
        hour_to_hour_result = Regex().search(TimeSheet().customize_timesheet_patterns("hour_to_hour", sign), line)
        if hour_to_hour_result is not False:
            if hour_to_hour_result[1] == "":
                hour_to_hour_result[1] = 0
            if hour_to_hour_result[3] == "":
                hour_to_hour_result[3] = 0

            time1 = int(hour_to_hour_result[0])*60 + int(hour_to_hour_result[1])
            time2 = int(hour_to_hour_result[2])*60 + int(hour_to_hour_result[3])
            if time2 < time1:
                time2 += 12*60
            return time2 - time1

        hour_and_minute_result = Regex().search(TimeSheet().customize_timesheet_patterns("hour_and_minute", sign), line)
        if hour_and_minute_result is not False:
            if hour_and_minute_result[1] == "":
                hour_and_minute_result[1] = 0
            time1 = int(hour_and_minute_result[0])*60 + int(hour_and_minute_result[1])
            return time1
        
        minutes_result = Regex().search(TimeSheet().customize_timesheet_patterns("minutes", sign), line)
        if minutes_result is not False:
            time1 = int(minutes_result[0])
            return time1
            
        
    def analyse_add_time(self, line):
        pass
