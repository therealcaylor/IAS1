# Write/test a function isSubstring(p, s) that checks whether the string p (pattern) is a substring of the string s, and returns a boolean result. Do not rely on built-in behaviors of the string class, other than string length calculation with len() and string indexing to retrieve.

def isSubstring(p, s):
    m = len(p)
    n = len(s)
    for i in range(n - m + 1):
        j = 0
        while (j < m):
            if (s[i + j] != p[j]):
                break
            j += 1
        if (j == m):
            return True
    return False

print(isSubstring('foo', 'hellofoo'))