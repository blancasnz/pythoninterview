

def merge(intervals):
    intervals.sort(key=lambda x: x.start)

    output = []
    for interval in intervals:
        if not output or output[-1].end < interval.start:
            output.append(interval)
        else:
            output[-1].end = max(output[-1].end, interval.end)
    return output
