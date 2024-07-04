def solution(myStr):
    myStr = myStr.replace('a', '\n').replace('b', '\n').replace('c', '\n').replace('\n', ' ')
    return myStr.split() if myStr.split() else ["EMPTY"]
