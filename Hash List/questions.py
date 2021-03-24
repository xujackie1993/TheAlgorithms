#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def longestsubstring(self, s):
        hashmap = {}
        start = 0
        ans = 0
        for i in range(s):
            if s[i] in hashmap:
                start = max(hashmap[s[i]], start)
            ans = max(ans, i - start + 1)
            hashmap[s[i]] = i + 1
        return ans

