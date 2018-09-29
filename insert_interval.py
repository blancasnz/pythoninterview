
class Interval(object):

    def __init__(self, start, end):
        self.start = start
        self.end = end


def insert(intervals, new_interval):
    start = new_interval.start
    end = new_interval.end
    left = right = 0
    while right < len(intervals):
        if start > intervals[right]:
            left += 1
            right += 1
        else:
            if end < intervals[right].start:
                break
            start = min(start, intervals[right.start])
            end = max(end, intervals[right].end)
            right += 1

    return intervals[:left] + [Interval(start, end)] + intervals[right:]
