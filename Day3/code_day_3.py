def getscore():
    score = {}
    for i in range(97, 123):
        score[chr(i)] = i - 96
    for i in range(65, 91):
        score[chr(i)] = i - 65+27
    return score

def betterSplit(a):
    return [a[i*3:i*3+3] for i in range(len(a)//3)]

def main():
    score = getscore()
    bags = sum([score[list(set(l[:len(l)//2]).intersection(set(l[len(l)//2:])))[0]] for l in open('input.sql').readlines()])
    print("Part 1 : {}".format(bags))
    bags = sum([score[list(set(b[0].strip('\n')).intersection(b[1].strip('\n')).intersection(b[2].strip('\n')))[0]] for b in betterSplit(open('input.sql').readlines())])
    print("Part 2 : {}".format(bags))
if __name__ == '__main__':
    main()