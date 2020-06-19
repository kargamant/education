from collections import OrderedDict, defaultdict, deque

N = 5000
with open('big_log.txt', 'r', encoding='utf-8') as file:
    raw_data = deque(file, maxlen=N)
print(raw_data)

data = OrderedDict()
spam = defaultdict(int)
for item in raw_data:
    ip = item[:-1]
    if not ip.startswith('192.168'):
        spam[ip] += 1
        data[ip] = 1
print(spam)
print(data)

data.update(spam)
with open('data.txt', 'w', encoding='utf-8') as file:
    for key, value in data.items():
        file.write(f'{key} - {value}\n')