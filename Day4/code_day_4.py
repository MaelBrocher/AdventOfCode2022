def sortTasks(tasks, exo1=True):
    s = 0
    for t in tasks:
        e1,e2 = t[0].split('-'), t[1].split('-')
        match exo1 :
            case True:
                if int(e1[0]) >= int(e2[0]) and int(e1[1]) <= int(e2[1]) or int(e2[0]) >= int(e1[0]) and int(e2[1]) <= int(e1[1]):
                    s +=1
            case False:
                tab = [0]*100
                for i in range(int(e1[0]),int(e1[1])+1):
                    tab[i] += 1
                for i in range(int(e2[0]),int(e2[1])+1):
                    tab[i] += 1
                s += 1 if tab.count(2) >= 1 else 0
    return s

def main():
    tasks = [l.strip('\n').split(',') for l in open('input.sql').readlines()]
    print("Part 1 : {}".format(sortTasks(tasks)))
    print("Part 2 : {}".format(sortTasks(tasks, False)))

if __name__ == '__main__':
    main()