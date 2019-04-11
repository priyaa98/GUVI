class FindHoliday:
    def __init__(self):
        self.days=input()
        self.days=self.days.split(" ")
    def finding(self):
        holidays=['Saturday','Sunday']
        for i in self.days:
            if i in holidays:
                print("yes")
            else:
                print("no")

fh=FindHoliday()
fh.finding()
