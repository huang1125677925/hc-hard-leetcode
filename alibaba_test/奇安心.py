class Solution:
    def house(self , person ):
        # write code here
        length = len(person)
        temp = [0]
        res = [1]*length
        for i in range(1, length):
            if person[i] == person[temp[-1]]:
                temp = [i]
                continue
            elif person[i] > person[temp[-1]]:
                res[i] = res[temp[-1]] + 1
                temp = [i]
            else:
                temp.append(i)
                for j in range(len(temp)-2, -1, -1):
                    res[temp[j]] = res[temp[j+1]] +1
        return sum(res)
    

print Solution().house([3,2,4])