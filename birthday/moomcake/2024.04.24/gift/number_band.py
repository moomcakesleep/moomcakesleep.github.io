import random as r


def judgment(guessnum,theband,minivalue,maxvalue):
    if guessnum >= maxvalue or guessnum <= minivalue:
        return 404 # 如果猜的数大于等于最大值或小于等于最小值，返回404（值异常）
    else:
        if guessnum == theband:
            return 0 # 如果猜的数等于炸弹，返回0（猜中炸弹）
        elif guessnum > theband:
            return 1 # 如果猜的数大于炸弹，返回1（大了）
        elif guessnum < theband:
            return -1 # 如果猜的数小于炸弹，返回-1（小了）

while True:
    judgment_result = """
Game:Number Band
Program:moomcakesleep
"""
    minivalue, maxvalue = 1, 100
    theband = r.randint(minivalue+1,maxvalue-1)

    while judgment_result != 0:
        guessnum = input("%d-%d:"%(minivalue, maxvalue))

        try:
            guessnum = int(guessnum)
        except ValueError:
            print("输入值异常，请重新输入")
            continue

        judgment_result = judgment(guessnum,theband,minivalue,maxvalue)

        if judgment_result == 404:
            print("请确保你的输入值处于区间[%d,%d]内"%(minivalue,maxvalue))
            continue
        elif judgment_result == 1:
            maxvalue = guessnum
        elif judgment_result == -1:
            minivalue = guessnum
        else:
            print("很不幸，你踩中了炸弹")
            the_choose_of_end = input("要继续吗\n1.继续    2.不了\n")
            if the_choose_of_end == "2":
                print("好叭qwq")
                exit()
