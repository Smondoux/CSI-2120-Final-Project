class Course:
    def __init__(self, name, courseid, days=None, times=None):
        self.name = name
        self.courseid = courseid
        self.days = days if days is not None else []
        self.times = times if times is not None else []
    

    # Getters
    def getName(self):
        return self.name

    def getCourseId(self):
        return self.courseid

    def getDays(self):
        return self.days

    def getTimes(self):
        return self.times

    def getSelectState(self):
        return self.selected
    
    # Setters
    def setName(self, name):
        self.name = name

    def setCourseId(self, courseid):
        self.courseid = courseid

    def setDays(self, days):
        if not isinstance(days, list):
            raise TypeError("days must be a list")
        self.days = days

    def setTimes(self, times):
        if not isinstance(times, list):
            raise TypeError("times must be a list")
        self.times = times

    

