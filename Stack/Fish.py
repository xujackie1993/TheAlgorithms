# -*- coding=utf-8 -*-
# 大鱼吃小鱼问题  假设鱼都停放在x轴上  两个列表  一个代表鱼的大小，一个表示鱼游动的方向。当方向相对时，大鱼会吃掉小鱼。 给定两个列表，得到最后剩下几条鱼

class Solution(object):

    def fish_eat(self, fishSize, fishDirection):
        fishNumber = len(fishSize)
        if fishNumber <= 1:
            return fishNumber
        left = 0
        right = 1
        t = []
        for i in range(0, fishNumber):
            # 当前鱼的情况  游动方向  大小
            curFishDirect = fishDirection[i]
            curFishSize = fishSize[i]

            # 当前的鱼是否被栈里的鱼吃点
            hasEat = False
            # 如果栈里有鱼 并且栈里鱼向左，当前鱼向右就有相遇可能
            while len(t) > 0 and fishDirection[t[-1]] == right and curFishDirect == left:
                # 如果当前鱼比栈里的鱼小  那么被吃掉  跳出while循环
                if fishSize[t[-1]] > curFishSize:
                    hasEat = True
                    break
                #  如果当前鱼比栈里的鱼大,就会把栈里的鱼吃掉那么需要弹栈
                t.pop()

            # 如果是新来的鱼，没有被吃掉，那么压入栈底
            if not hasEat:
                t.append(i)
        
        return len(t)