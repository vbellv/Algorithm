def solution(hp):
    lv1, lv2, lv3 = 0, 0, 0
    while hp > 0:
        lv3 = hp // 5
        hp = hp - 5 * lv3
        lv2 = hp // 3
        hp = hp - 3 * lv2
        lv1 = hp
        break
    return (lv1+lv2+lv3)