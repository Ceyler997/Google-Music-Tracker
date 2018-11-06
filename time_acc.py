'''Time accumulator class'''


def upd(smaller_val, larger_val, threshold):
    '''
    Increments larger value in smaller_val // threshold times
    and decreases smaller_val on a corresponding value'''
    if smaller_val >= threshold:
        larger_val += smaller_val // threshold
        smaller_val = smaller_val % threshold

    return smaller_val, larger_val


class TimeAcc:
    '''Class for accumulating time'''
    def __init__(self):
        self.mls = 0
        self.sec = 0
        self.min = 0
        self.hours = 0
        self.days = 0
        self.years = 0

    def add(self, acc_ms):
        '''Adds acc_ms milliseconds to the accumulated time'''
        self.mls += acc_ms

        (self.mls, self.sec) = upd(self.mls, self.sec, 1000)
        (self.sec, self.min) = upd(self.sec, self.min, 60)
        (self.min, self.hours) = upd(self.min, self.hours, 60)
        (self.hours, self.days) = upd(self.hours, self.days, 24)
        (self.days, self.years) = upd(self.days, self.years, 365)

    def __str__(self):
        months = int(self.days // (365 / 12))
        days = self.days % (365 / 12)

        weeks = int(days // 7)
        days %= 7

        hours = (days % 1) * 24 + self.hours
        days = int(days // 1)

        minutes = (hours % 1) * 60 + self.min
        hours = int(hours // 1)

        seconds = (minutes % 1) * 60 + self.sec
        minutes = int(minutes // 1)

        mls = (seconds % 1) * 1000 + self.mls
        seconds = int(seconds // 1)

        mls = round(mls)

        (mls, seconds) = upd(mls, seconds, 1000)
        (seconds, minutes) = upd(seconds, minutes, 60)
        (minutes, hours) = upd(minutes, hours, 60)
        (hours, days) = upd(hours, days, 24)
        (days, weeks) = upd(days, weeks, 7)

        result = 'Years: ' + str(self.years) + '\n'
        result += 'Months: ' + str(months) + '\n'
        result += 'Weeks: ' + str(weeks) + '\n'
        result += 'Days: ' + str(days) + '\n'
        result += 'Hours: ' + str(hours) + '\n'
        result += 'Minutes: ' + str(minutes) + '\n'
        result += 'Seconds: ' + str(seconds) + '\n'
        result += 'Ms: ' + str(mls) + '\n'
        return result

    def reset(self):
        '''Resets accumulator back to zero'''
        self.mls = 0
        self.sec = 0
        self.min = 0
        self.hours = 0
        self.days = 0
        self.years = 0
