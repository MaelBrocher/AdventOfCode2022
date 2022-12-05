def getscore():
    score = {}
    for i in range(97, 123):
        score[chr(i)] = i - 96
    for i in range(65, 91):
        score[chr(i)] = i - 65+27
    return score

def betterSplit(a):
    b = []
    tmp = []
    for y,s in enumerate(a):
        if y%3 == 0 and y != 0:
            b.append(tmp)
            tmp = []
        tmp.append(s.strip('\n'))
    b.append(tmp)
    return b

def main():
    score = getscore()
    bags = sum([score[list(set(l[:len(l)//2]).intersection(set(l[len(l)//2:])))[0]] for l in open('input.sql').readlines()])
    print("Part 1 : {}".format(bags))
    bags = sum([score[list(set(b[0]).intersection(b[1]).intersection(b[2]))[0]] for b in betterSplit(open('input.sql').readlines())])
    print("Part 2 : {}".format(bags))
if __name__ == '__main__':
    main()