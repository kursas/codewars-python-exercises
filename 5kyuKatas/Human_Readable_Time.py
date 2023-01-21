# Solution 1
def make_readable(seconds):
    h = seconds // 3600
    m = (seconds - h * 3600) // 60
    s = seconds - (h * 3600) - (m * 60)
    return f"{h:0>2d}:{m:0>2d}:{s:0>2d}"



# Solution 2
def make_readable(seconds):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
