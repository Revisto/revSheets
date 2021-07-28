from datetime import datetime

class Time:
    def current_minutes(self):
        now = datetime.now()
        hour = now.hour
        if hour > 12:
            hour -= 12 
        return hour*60 + now.minute
    
    def convert_minutes_to_hours_and_minutes(self, minutes):
        hours = minutes // 60
        left_minutes = minutes % 60
        return hours, left_minutes