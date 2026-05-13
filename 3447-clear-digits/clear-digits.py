class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        sb=[]
        for i in s:
            if i.isdigit():
                sb.pop()
            else:
                sb.append(i)

        return "".join(sb)
        