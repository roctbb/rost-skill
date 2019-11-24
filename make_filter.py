full = list(filter(lambda x: len(x) < 1024, open('all.txt').read().split('<|endoftext|>')))

banned = ['хуй', 'хуем', 'хуя', 'хую', 'бляд', 'ебат', 'ебал', 'ебет', 'ебёт', 'пизд', 'охуе', 'охуи']

def check(line):
    for ban in banned:
        if ban in line.lower():
            return True
    return False

with open('filtered.txt', 'w') as f:
    for anek in full:
        if check(anek):
            continue
        f.write(anek + '<|endoftext|>')