if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
    scoresSet = set([s[1] for s in students])
    scores = sorted(scoresSet)
    minscore = scores[1]        
    lwgr = sorted([s[0] for s in students if s[1] == minscore])
    
    for st in lwgr:
        print(st)