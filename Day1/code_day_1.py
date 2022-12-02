def main():
    f = open("input.sql",'r').read()
    elves = [ sum([int(c) for c in cal.split('\n')]) for cal in f.split('\n\n')]
    print("Part 1 = {}".format(max(elves)))
    elves.sort()
    print("Part 2 = {}".format(sum(elves[-3:])))    
    return

if __name__ == '__main__':
    main()