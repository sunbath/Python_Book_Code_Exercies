import pprint

# Data
text = '''
Call me Ishmael. Some years ago - never mind how long precisely - having
 little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
 the circulation. - Moby Dick'''

# Find any word with length > 3
lines = [line for line in text.split('\n')]
#pprint.pprint(lines)
words = [[x for x in line.split(' ') if len(x)>3] for line in text.split('\n')]
pprint.pprint(words)
