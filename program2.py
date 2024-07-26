def decode_message( s: str, p: str) -> bool:

# write your code here
  
        return False

def isMatch(message, pattern):
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
print(isMatch("aa", "a"))        
print(isMatch("aa", "*"))        
print(isMatch("cb", "?a"))       
print(isMatch("adceb", "*a*b"))  
print(isMatch("acdcb", "a*c?b")) 