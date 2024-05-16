#srbridge.com
#https://github.com/srbridgecom
#https://www.facebook.com/srbridge
#https://www.linkedin.com/in/r-bridge-3baa332a4/
#Python
#Given two strings, S1 and S2, the task is to find the
#length of the Longest Common Subsequence, i.e. 
#longest subsequence present in both of the strings. 
#the longest common subsequence (LCS) is defined 
#as the longest subsequence which is common in 
#all given input sequences.
#EXAMPLE:
# Input: S1 = “AGGTAB”, S2 = “GXTXAYB”
# Output: 4
# Explanation: The longest subsequence which is present in both strings is “GTAB”.
# Input: S1 = “BD”, S2 = “ABCD”
# Output: 2
# Explanation: The longest subsequence which is present in both strings is “BD”.

#ANSWER - using recursion
def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs(X, Y, m-1, n-1)
    else:
        return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))
    
#perform the op
if __name__ == '__main__':
    S1 = "AGGTAB"
    S2 = " GXTXAYB"
    print("length of LCS is", lcs(S1, S2, len(S1), len(S2)))
