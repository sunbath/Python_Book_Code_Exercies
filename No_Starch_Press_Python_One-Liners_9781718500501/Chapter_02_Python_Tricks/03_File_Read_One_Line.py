print([line for line in open("03.txt")])
print(len([line for line in open('03.txt')]))
print([[x for x in line.split(' ') if len(x) >= 10] for line in open('03.txt')])
