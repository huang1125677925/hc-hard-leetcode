#encodign=utf-8
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        nums_list = []
        while num:
            temp, num = num%1000, num/1000
            if temp and num:
                nums_list.append(temp)
            elif num and not temp:
                nums_list.append(0)
            else:
                nums_list.append(temp)
                break
        
        
        
        res = []
        for i in range(len(nums_list)):
            res.append(self.make(nums_list[i], i))
        
        
        
        return ' '.join(res[::-1])
    
    def make(self, number, i):
        suffix = ['', 'Thousand', 'Million', 'Billion']
        word = ['zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        words = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        word_1 = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen',  'Eighteen', 'Nineteen']
        char_list = []
        if number == 0:
            return ''
        res = []
        if number/100:
            hundred_char = number/100
            number = number%100
            res.extend([word[hundred_char], 'Hundred'])
        if number/10:
            ten_char = number/10
            number = number%10
            if ten_char:
                if ten_char == 1:
                    res.append(word_1[number])
                else:
                    res.append(words[ten_char])
                    if number:
                        res.append(word[number])
        
        elif number:
            res.append(word[number])
        
        if i > 0 :
            res.append(suffix[i])
        
        return ' '.join(res)
    

print Solution().numberToWords(1230)