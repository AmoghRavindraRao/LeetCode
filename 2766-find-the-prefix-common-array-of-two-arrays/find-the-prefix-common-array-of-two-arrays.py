class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        dic = {}
        c = []
        for i in range(len(A)):
            if A[i] in dic:
                dic[A[i]] += 1
            else:
                dic[A[i]] = 0
            if B[i] in dic:
                dic[B[i]] += 1
            else:
                dic[B[i]] = 0
            total = sum(dic.values()) 
            c.append(total)
        return c