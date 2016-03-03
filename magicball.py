import random
def getNo(answerNo):
    if answerNo == 1:
        return 'It is Cer'
    elif answerNo == 2:
        return 'It is Dec'
    elif answerNo == 3:
        return 'Yes'
    elif answerNo == 4:
        return 'Reply hazy try again'
    elif answerNo == 5:
        return 'Ask again later'
    elif answerNo == 6:
        return 'Concentrate and ask again'
    elif answerNo == 7:
        return 'My reply is no'
    elif answerNo == 8:
        return 'Outlook not so good'
    elif answerNo == 9:
        return 'Very doubtful'
#r = 
#fortune = getNo(r)
print(getNo(random.randint(1,9)))
