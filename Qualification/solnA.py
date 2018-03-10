import sys
import pendulum


IMPOSSIBLE = "IMPOSSIBLE"


def solve_one(pancakes, flippersize):
    n = len(pancakes)
    flipcount = 0
    sliding_window = (0, flippersize)
    if n == flippersize:
        if pancakes.count(1) == n:
            return 0
        if pancakes.count(0) == n:
            return 1
        return IMPOSSIBLE
    while (pancakes.count(1) < n):
        start, end = sliding_window
        if end > n:
            return IMPOSSIBLE
        if not pancakes[start]:
            # If the left pancake is unhappy, flip
            pancakes[start: end] = map(lambda x: not x, pancakes[start: end])
            flipcount += 1
        sliding_window = (start + 1, end + 1)
    return flipcount


def solve(fname):
    fp = open(fname)
    next(fp)
    caseno = 1
    with open("output_%s_%s" % (fname, pendulum.utcnow().isoformat()), 'a') as outf:
        for line in fp:
            pancakes, flippersize = line.strip().split()
            pancakes = map(int, list(pancakes.replace('+', '1').replace('-', '0')))
            outf.write("Case #{}: {}{}".format(
                caseno,
                solve_one(pancakes, int(flippersize)),
                '\n')
            )
            caseno += 1


if __name__ == "__main__":
    solve(sys.argv[1])
