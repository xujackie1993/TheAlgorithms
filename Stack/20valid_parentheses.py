# -*- coding=utf-8 -*-

#[20] 有效的括号
# 栈 后进先出
# 配对 消除


class Solution(object):
    def is_valid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s) == 0:
            return True
        if len(s) % 2 == 1:
            return False
        
        t = []
        for c in s:
            if c == "{" or c == "[" or c == "(":
                t.append(c)
            elif c == "]":
                last = t.pop() if t else "#"
                if last != "[":
                    return False
            elif c == "}":
                last = t.pop() if t else "#"
                if last != "{":
                    return False
            elif c == ")":
                last = t.pop() if t else "#"
                if last != "(":
                    return False
            else:
                return False

        return not t

    
    def isVaild_1(self, s):
        """
        使用中间变量
        """
        if not s or len(s) == 0:
            return True
        if len(s) % 2 == 1:
            return False
        tempNumber = 0
        for c in s:
            if c == "{":
                tempNumber += 1
            elif c == "}":
                tempNumber -= 1
                if tempNumber < 0:
                    return False
        return tempNumber == 0