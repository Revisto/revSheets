import re

class Regex:
    def search(self, pattern, text, flag=re.M):
        search_result = re.search(pattern, text, flag)
        if search_result is None:
            return False
        return list(search_result.groups())