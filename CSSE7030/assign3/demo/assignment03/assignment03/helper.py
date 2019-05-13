#!/usr/bin/env python3
def display_time(interval):
    if interval < 1 * 60:
        return "a few seconds ago"
    elif interval < 2 * 60:
        return "a minute ago"
    elif interval < 60 * 60:
        return "{} minutes ago".format(int(interval / 60))
    elif interval < 2 * 60 * 60:
        return "1 hour ago"
    else:
        return "{} hours ago".format(int(interval / (60 * 60)))

