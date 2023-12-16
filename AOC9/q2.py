from queue import Queue

with open("input.txt", "r") as f:
    m = [list(l.strip()) for l in f]

    n = {
        "|": [(0, -1), (0, 1)],
        "-": [(-1, 0), (1, 0)],
        "L": [(0, -1), (1, 0)],
        "J": [(0, -1), (-1, 0)],
        "7": [(-1, 0), (0, 1)],
        "F": [(1, 0), (0, 1)],
    }

    x, y = None, None

    for yi, line in enumerate(m):
        for xi, c in enumerate(line):
            if c == "S":
                x, y = xi, yi
                break

    assert x is not None
    assert y is not None

    q = Queue()

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        c = m[y + dy][x + dx]
        if c in n:
            for dx2, dy2 in n[c]:
                if x == x + dx + dx2 and y == y + dy + dy2:
                    q.put((1, (x + dx, y + dy)))

    dists = {(x, y): 0}
    assert q.qsize() == 2

    while not q.empty():
        d, (x, y) = q.get()

        if (x, y) in dists:
            continue

        dists[(x, y)] = d

        for dx, dy in n[m[y][x]]:
            q.put((d + 1, (x + dx, y + dy)))

    inside_tiles = set()

    for y, line in enumerate(m):
        for x, c in enumerate(line):
            if (x, y) not in dists and c != "S":
                inside_tiles.add((x, y))

    for y, line in enumerate(m):
        for x, c in enumerate(line):
            if c == "." and (x, y) in inside_tiles:
                queue = [(x, y)]
                visited = set()

                while queue:
                    cur_x, cur_y = queue.pop(0)
                    visited.add((cur_x, cur_y))

                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        new_x, new_y = cur_x + dx, cur_y + dy
                        if (
                            0 <= new_x < len(line)
                            and 0 <= new_y < len(m)
                            and (new_x, new_y) not in visited
                            and (new_x, new_y) in inside_tiles
                        ):
                            queue.append((new_x, new_y))

                inside_tiles -= visited

    enclosed_tile_count = len(inside_tiles)
    print(f"Tiles enclosed by the loop: {enclosed_tile_count}")
