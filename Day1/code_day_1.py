def main():
    elves = [ sum([int(c) for c in cal.split('\n')]) for cal in open("input.sql",'r').read().split('\n\n')]
    print("Part 1 = {}".format(max(elves)))
    elves.sort()
    print("Part 2 = {}".format(sum(elves[-3:])))

if __name__ == '__main__':
    main()