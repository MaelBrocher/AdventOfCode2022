O_Rock = "A"
O_Paper = "B"
O_Cissors = "C"
M_Rock = "X"
M_Paper= "Y"
M_Cissors = "Z"

def fuse(Opp, Me):
    return Opp + " " + Me + "\n"

def main():
    outcome = {fuse(O_Cissors, M_Cissors):3+3, fuse(O_Paper, M_Paper):2+3, fuse(O_Rock, M_Rock):1+3,fuse(O_Cissors, M_Rock):6+1, fuse(O_Paper, M_Cissors):6+3, fuse(O_Rock, M_Paper):6+2, fuse(O_Cissors, M_Paper):0+2, fuse(O_Paper, M_Rock):0+1, fuse(O_Rock, M_Cissors):0+3}
    print("Part 1 : {}".format( sum(outcome[l] for l in open("input.sql", "r").readlines())))

    win = {O_Rock : M_Paper, O_Paper : M_Cissors, O_Cissors : M_Rock}
    lose = {O_Rock : M_Cissors, O_Paper : M_Rock, O_Cissors : M_Paper}
    draw = {O_Rock: M_Rock, O_Paper : M_Paper, O_Cissors: M_Cissors}
    score = 0
    for l in open("input.sql", "r").readlines():
        Opp_move = l.split(' ')[0];
        match l.split(' ')[1].strip('\n') :
            case "Y" :
                score += outcome[fuse(Opp_move, draw[Opp_move])]
            case "X" :
                score += outcome[fuse(Opp_move, lose[Opp_move])]
            case "Z" :
                score += outcome[fuse(Opp_move, win[Opp_move])]
    print("Part 2 : {}".format(score))

if __name__ == '__main__':
    main()