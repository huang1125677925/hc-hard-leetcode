class Solution:
    def numberofprize(self , a , b , c ):
        # write code here
        temp = [a, b, c]
        temp.sort()
        res =temp[0] + (temp[2]+temp[1]-2*temp[0])/4

class Solution:
    def numberofprize(self, a, b, c):
        # write code here
        temp = [a, b, c]
        temp.sort()
        res = temp[0]
        temp = [temp[1]-temp[0], temp[2]-temp[0]]
        if temp[0] == 0:
            return res + temp[1]/5
        elif 3*temp[0] <= temp[1]:
            return res + temp[0] + (temp[1]-3*temp[0])/5
        else:
            return res + (temp[1]+temp[0])/4
    
print Solution().numberofprize(9, 3, 3)