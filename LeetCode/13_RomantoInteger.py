class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        exceptions = {'IV': 4,
                     'IX': 9,
                     'XL': 40,
                     'XC': 90,
                     'CD' : 400,
                     'CM': 900}
        roman_numeral = {'I': 1,
                         'V': 5,
                         'X': 10,
                         'L': 50,
                         'C': 100,
                         'D': 500,
                         'M': 1000
        }
        for key in exceptions.keys():
            start = s.find(key)
            if start != -1:
                output += exceptions[key]
                s = s[:start] + s[start+2:]
        
        for num in roman_numeral.keys():
            while True:
                start = s.find(num)
                if start == -1:
                    break
                else:
                    output += roman_numeral[num]
                    s = s[:start] + s[start+1:]
        
        return output
