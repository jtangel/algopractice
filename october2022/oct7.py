# Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

def breakingRecords(scores):
    timesRecordsBroke = [0,0]
    minScore = scores[0]
    maxScore = scores[0]
    for i in range(len(scores)):
        if scores[i] > maxScore:
            maxScore = scores[i]
            timesRecordsBroke[0] += 1
        if scores[i] < minScore:
            minScore = scores[i]
            timesRecordsBroke[1] += 1
    return timesRecordsBroke

print(breakingRecords([10,5,20,20,4,5,2,25,1]))