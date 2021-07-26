from datetime import datetime

class Time:
    def current_minutes(self):
        now = datetime.now()
        hour = now.hour
        if hour > 12:
            hour -= 12 
        return hour*60 + now.minute
