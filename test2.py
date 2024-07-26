import unittest
from program2 import decode_message
'''
class TestDecoder(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(decode_message("aa", "a"), False)

    def test_case2(self):
        self.assertEqual(decode_message("aa", "*"), True)

    def test_case3(self):
        self.assertEqual(decode_message("cb", "?a"), False)

    def test_case4(self):
        self.assertEqual(decode_message("abc", "?b?"), True)

if __name__ == '__main__':
    unittest.main() '''

def decode_message(message, pattern):
    m, n = len(message), len(pattern)
    
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    for i in range(1, n + 1):
        if pattern[i-1] == '*':
            dp[i][0] = dp[i-1][0]
        else:
            break
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if pattern[i-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
            elif pattern[i-1] == '?':
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] and (pattern[i-1] == message[j-1])
    
    return dp[n][m]

# Test cases
print(decode_message("aa", "a"))        
print(decode_message("aa", "*"))        
print(decode_message("cb", "?a"))       
print(decode_message("abc", "?b?"))     
