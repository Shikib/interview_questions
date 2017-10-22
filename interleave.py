def isInterleave(s1, s2, s3):
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """
    # (i,j) -> boolean
    dp = {}
    def _solve(i, j):
        if i+j == len(s3):
            return i == len(s1) and j == len(s2)
        elif i == len(s1):
            return s2[j:] == s3[i+j:]
        elif j == len(s2):
            return s1[i:] == s3[i+j:]
        
        if (i,j) in dp:
            return dp[(i,j)]
    
        if s1[i] == s3[i+j] and s2[j] == s3[i+j]:
            dp[(i,j)] = _solve(i+1,j) or _solve(i,j+1)
        elif s1[i] == s3[i+j]:
            dp[(i,j)] = _solve(i+1,j)
        elif s2[j] == s3[i+j]:
            dp[(i,j)] = _solve(i,j+1)
        else:
            dp[(i,j)] = False
        
        return dp[(i,j)]
    
    return _solve(0,0)
