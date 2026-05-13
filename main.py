from collections import deque

def chk(z, w):
    h = [[] for _ in range(z)]
    for a, b, c in w:
        h[a].append((b, c))
        h[b].append((a, c))

    q = [-1] * z

    for s in range(z):
        if q[s] != -1:
            continue

        q[s] = 0
        d = deque([s])

        while d:
            x = d.popleft()
            for y, t in h[x]:
                r = q[x] ^ t
                if q[y] == -1:
                    q[y] = r
                    d.append(y)
                elif q[y] != r:
                    return False

    return True

z = 4
w = [
    (0, 1, 0),  # 0 и 1 одинаковые
    (1, 2, 1),  # 1 и 2 разные
    (2, 3, 0),  # 2 и 3 одинаковые
    (0, 3, 1),  # 0 и 3 разные
]

print(chk(z, w))  # True


w2 = [
    (0, 1, 0),  # 0 и 1 одинаковые
    (1, 2, 0),  # 1 и 2 одинаковые
    (0, 2, 1),  # 0 и 2 разные
]

print(chk(z, w2))  # False
