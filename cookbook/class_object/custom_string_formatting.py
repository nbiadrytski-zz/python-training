formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = formats[code]
        return fmt.format(d=self)


d = Date(2019, 3, 4)

print(format(d))  # 2019-3-4

print(format(d, 'mdy'))  # 3/4/2019

print("The date is {:dmy}".format(d))
