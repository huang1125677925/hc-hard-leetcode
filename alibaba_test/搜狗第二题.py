class Solution:
    def getHouses(self , t , xa ):
        # write code here
        temp = []
        for i in range(0, len(xa), 2):
            temp.append([xa[i]-xa[i+1]/2, xa[i]+xa[i+1]])
        res = 0
        for i in range(1, len(temp)):
            temp2 = temp[i][0]- temp[i-1][1]
            if temp2 == t:
                res +=1
            elif temp2 > t:
                res +=2
        return res+2
    
    
print Solution().getHouses(2, [-1, 4, 5, 2])