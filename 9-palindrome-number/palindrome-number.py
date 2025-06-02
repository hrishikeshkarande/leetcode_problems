class Solution:
    def isPalindrome(self, x: int) -> bool:
      #Negative numbers are not palindromes
      if x < 0:
        return False
      # Numbers ending with 0 are not palindromes unless the number is 0
      if x % 10 == 0 and x != 0:
        return False

      reversed_num = 0
      original = x

      while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x=x//10 # can also be written as x//=10

        '''
| Iteration | `x` | `digit` | `reversed_num`     |
| --------- | --- | ------- | ------------------ |
| 1         | 123 | 3       | 0 \* 10 + 3 = 3    |
| 2         | 12  | 2       | 3 \* 10 + 2 = 32   |
| 3         | 1   | 1       | 32 \* 10 + 1 = 321 |

        '''
      
      return original == reversed_num 
     
            
        