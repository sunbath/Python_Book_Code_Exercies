# Data
txt = ['lambda functions are anonymous functions.',
       'anonymous functions dont have a name.', 'functions are objects in Python.']
# One-Liner
mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt)
# Result
#print(list(mark))

mark_list = [(True, line) if 'anonymous' in line else(False, line) for line in txt]
print(mark_list)
