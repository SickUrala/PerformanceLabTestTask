import sys

n, m = int(sys.argv[1]), int(sys.argv[2])
path = []
current = 0

while True:
    path.append(current + 1)
    current = (current + m - 1) % n
    if current == 0:
        break

print(''.join(map(str, path)))
