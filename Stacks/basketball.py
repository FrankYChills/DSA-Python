def calcScore(operations):
    score = [];
    for ch in operations:
        if ch == "D":
            double = 2 * score[-1]
            score.append(double)
        elif ch == "+":
            last2sum = score[-1] + score[-2]
            score.append(last2sum)
        elif ch == "C":
            score.pop()
        else:
            score.append(int(ch))
    print(sum(score))
    return sum(score)



calcScore(["5", "2", "C", "D", "+"])
