class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        leng = len(s)
        i = 0
        while True:
            comb = False
            # all combinations as following
            if leng>1:
                if s[0:2]=='IV': i +=4; comb = True
                elif s[0:2]=='IX': i += 9; comb = True
                elif s[0:2]=='XL': i += 40; comb = True
                elif s[0:2]=='XC': i += 90; comb = True
                elif s[0:2]=='CD': i += 400; comb = True
                elif s[0:2]=='CM': i += 900; comb = True
            
            if comb==True: 
                leng -= 2
                s = s[2:] # if s=='IV', then s[2:] will be ''. I made a mistake using s as break/return condition, bad choice
            else:
                if s[0]=='I': i +=1
                elif s[0]=='V': i += 5
                elif s[0]=='X': i += 10
                elif s[0]=='L': i += 50
                elif s[0]=='C': i += 100
                elif s[0]=='D': i += 500
                elif s[0]=='M': i += 1000
                leng -= 1
                s = s[1:]
            if leng==0: return i # return result when no more letter
