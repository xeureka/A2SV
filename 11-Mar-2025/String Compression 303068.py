# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:

    def compress(self, chars: List[str]) -> int:


        i, j, length = 0, 0, len(chars)



        while i < length:


            i_next = i + 1

            while i_next < length and chars[i_next] == chars[i]:

                i_next += 1



            chars[j] = chars[i]

            j += 1



            if i_next - i > 1:


                count = str(i_next - i)

                for char in count:

                    chars[j] = char

                    j += 1



            i = i_next



        return j