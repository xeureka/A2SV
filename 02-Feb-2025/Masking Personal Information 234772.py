# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:

        def mask_email(email:str):
            new = email[0].lower()

            ast_count = 0
            

            left,right = 0,1

            while right <= len(email[1:]):
                if email[right] == '@':
                    new += email[left:].lower()
                    break
                else:
                    if ast_count < 5:
                        for i in range(5):
                            new += '*'
                            ast_count += 1
    


                left += 1
                right += 1
            
            return new
        
        def mask_phone(phone:str):
            n = 0

            for i in phone:
                if i.isdigit():
                    n += 1

            country_code = n - 10
            last_four = ''

            for i in reversed(phone):
                if len(last_four) < 4 and i.isdigit():
                    last_four += i
            


            if country_code == 0:
                return f'***-***-{last_four[::-1]}'
            
            elif country_code == 1:
                return f'+*-***-***-{last_four[::-1]}'
            
            elif country_code == 2:
                return f'+**-***-***-{last_four[::-1]}'
            else:
                return f'+***-***-***-{last_four[::-1]}'

        if '@' in s:
            return mask_email(s)
        else:
            return mask_phone(s)

