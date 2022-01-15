class Solution():


    def romanToInt(self, s: str) -> int:
        """
        Link to LeetCode: https://leetcode.com/problems/roman-to-integer/

        Args:
            s (str): roman string to convert to integer

        Returns:
            int: integer based on input roman string
        """
        result = 0
        romanToIntDict = {
            'M':1000,
            'D':500,
            'C':100,
            'L':50,
            'X':10,
            'V':5,
            'I':1}
        skip_next = False
        for idx in range(len(s)):
            if skip_next: 
                skip_next = False
                continue
            letter = s[idx]
            
            if idx < len(s)-1:
                next_letter = s[idx+1]
                if letter == 'I' and next_letter == 'V': 
                    result += 4
                    skip_next = True
                elif letter == 'I' and next_letter == 'X': 
                    result += 9
                    skip_next = True
                    
                if letter == 'X' and next_letter == 'L': 
                    result += 40
                    skip_next = True
                elif letter == 'X' and next_letter == 'C': 
                    result += 90
                    skip_next = True
                
                if letter == 'C' and next_letter == 'D': 
                    result += 400
                    skip_next = True
                elif letter == 'C' and next_letter == 'M': 
                    result += 900
                    skip_next = True
            
            if not skip_next: result += romanToIntDict[letter]
            # to ckeck output
            #print(f'idx {idx} letter roman {letter} letter int {romanToIntDict[letter]} result {result} ')

        return result