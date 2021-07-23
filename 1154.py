from datetime import datetime


class Solution:
    def dayOfYear(self, date: str) -> int:
        d = datetime.strptime(date, "%Y-%m-%d")
        return d.timetuple().tm_yday
